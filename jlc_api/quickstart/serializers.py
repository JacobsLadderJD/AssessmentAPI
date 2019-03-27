from django.contrib.auth.models import User, Group
from jlc_api.quickstart.models import Student, Evaluator, Evaluation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'code', 'status', 'first_name', 'last_name', \
                'birthdate', 'gender')

class EvaluatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluator
        fields = ('url', 'first_name', 'last_name')

class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('url', 'student_id', 'evaluator_id', 'created_at', 'edited_at')

