# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import viewsets
from jlc_api.quickstart import models
import jlc_api.quickstart.serializers as local_serializers

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = local_serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = local_serializers.GroupSerializer

class AuthenticatedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated!'}
        return Response(content)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = local_serializers.StudentSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluation.objects.all()
    serializer_class = local_serializers.EvaluationSerializer

# Returns students with the substring included their name
def studentsWithName(request, substring):

    # If there is a partial student name to search
    if substring:
        # QuerySet of student with substring in first or last name
        students = models.Student.objects.filter( \
                Q(firstname__icontains=substring) | \
                Q(lastname__icontains=substring))
    else:
        # If no substring to match, QuerySet of all students
        students = models.Student.objects.all()

    serialized = serializers.serialize('json', students, \
            fields=('firstname','lastname'))
    return HttpResponse(serialized)
