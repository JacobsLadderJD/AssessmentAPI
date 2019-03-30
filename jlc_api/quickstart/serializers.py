from django.contrib.auth.models import User, Group
from jlc_api.quickstart.models import Student, Evaluator, Evaluation
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'evaluator')
        depth = 1

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'code', 'status', 'firstName', 'lastName', \
                'birthdate', 'gender')

class EvaluatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluator
        fields = ('id', 'user', 'firstName', 'lastName')
        depth = 1

class EvaluationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'
        depth = 1

class EvaluationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('id', 'studentId', 'evaluatorId', 'createdAt', 'editedAt')
        depth = 1
