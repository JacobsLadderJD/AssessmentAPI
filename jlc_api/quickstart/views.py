# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from jlc_api.quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AuthenticatedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated!'}
        return Response(content)

# Returns students with the substring included their name
def studentsWithName(request, substring):
    # Stub
    return HttpResponse('No students')
