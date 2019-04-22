# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from jlc_api.quickstart import models
import jlc_api.quickstart.serializers as local_serializers
import csv

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create': 
            return local_serializers.UserCreateSerializer
        else:
            return local_serializers.UserListSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = local_serializers.GroupSerializer
    permission_classes = [IsAuthenticated]

class AuthenticatedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated!'}
        return Response(content)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all().order_by('lastName', 'firstName')
    serializer_class = local_serializers.StudentSerializer
    permission_classes = [IsAuthenticated]

class EvaluatorViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluator.objects.all().order_by('lastName', 'firstName')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create': 
            return local_serializers.EvaluatorCreateSerializer
        else:
            return local_serializers.EvaluatorListSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluation.objects.all().order_by('-editedAt', \
            'student__lastName', 'student__firstName', '-createdAt')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return local_serializers.EvaluationListSerializer
        elif self.action == 'create':
            return local_serializers.EvaluationCreateSerializer
        elif self.action == 'retrieve':
            return local_serializers.EvaluationRetrieveSerializer
        else:
            return local_serializers.EvaluationSerializer

# Returns CSV render of input evaluation id
def exportEvaluation(request, eval_id):

    # If no eval_id was specified
    if not eval_id:
        return HttpResponseBadRequest('No evaluation id given.')

    # Get the evaluation with that id
    try:
        evaluation = models.Evaluation.objects.get(pk=int(eval_id))
    except:
        return HttpResponseBadRequest('No evaluation found with that id.')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # Get just the sections of the evaluation
    sections = [
            evaluation.notesSection,
            evaluation.reflexSection,
            evaluation.tactilitySection,
            evaluation.auditorySection,
            evaluation.visualSection,
            evaluation.manualSection,
            evaluation.languageSection,
            evaluation.mobilitySection,
            evaluation.sensorySection,
            evaluation.sensitivitiesSection
    ]

    sections = [section for section in sections if 'startRow' in section]

    writer = csv.writer(response)
    writer.writerow(sections)

    return response

