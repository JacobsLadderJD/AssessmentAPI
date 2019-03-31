from django.contrib.auth.models import User, Group
from jlc_api.quickstart.models import Student, Evaluator, Evaluation
from rest_framework import serializers
import datetime


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

class EvaluatorNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluator
        fields = ('id', 'firstName', 'lastName')

class UserListSerializer(serializers.ModelSerializer):
    evaluator = EvaluatorNestedSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'evaluator')

class UserCreateSerializer(serializers.ModelSerializer):
    evaluator = serializers.PrimaryKeyRelatedField(queryset=Evaluator.objects.all())
    class Meta:
        model = User
        fields = ('username','password','email','evaluator')

class EvaluatorListSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer()
    class Meta:
        model = Evaluator
        fields = ('id', 'firstName', 'lastName', 'user')

class EvaluatorCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Evaluator
        fields = ('firstName','lastName','user')

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

class EvaluationCreateSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    evaluator = serializers.PrimaryKeyRelatedField(queryset=Evaluator.objects.all())
    class Meta:
        model = User
        fields = ('student','evaluator', 'id')

    def create(self, validated_data):
        today = datetime.date.today()
        evaluation = Evaluation(
                student=validated_data['student'],
                evaluator=validated_data['evaluator'],
                createdAt=today,
                editedAt=today
        )
        evaluation.save()
        return evaluation
