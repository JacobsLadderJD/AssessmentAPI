from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# From https://www.django-rest-framework.org/api-guide/authentication/
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M','Male'), ('F','Female')])
    diagnosis = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    # One-to-many relationship to Evaluation in definition of Evaluation

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    evaluator = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    # Currently stub - more to be added
