from django.contrib.auth.models import User, Group
from jlc_api.quickstart.models import Student, Evaluator, Evaluation
from rest_framework import serializers


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

class EvaluatorNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluator
        fields = ('id', 'firstName', 'lastName')

class UserSerializer(serializers.ModelSerializer):
    evaluator = EvaluatorNestedSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'evaluator')

class EvaluatorSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer()
    class Meta:
        model = Evaluator
        fields = ('id', 'firstName', 'lastName', 'user')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'code', 'status', 'firstName', 'lastName', \
                'birthdate', 'gender')

class EvaluationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'
        depth = 1

class EvaluationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('id', 'student', 'evaluator', 'createdAt', 'editedAt')
        depth = 1
