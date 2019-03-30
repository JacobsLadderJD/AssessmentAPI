from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from ..quickstart import json_defaults

# From https://www.django-rest-framework.org/api-guide/authentication/
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Student(models.Model):
    code = models.CharField(max_length=4, blank=True, choices=[
            ('ADHD','Attention-Deficit/Hyperactivity Disorder'),
            ('ASD','Autism Spectrum Disorder'),
            ('BI1','Brain Injury Level 1'),
            ('BI2','Brain Injury Level 2'),
            ('BI3','Brain Injury Level 3'),
            ('DS','Down Syndrome'),
            ('EDBS','Emotional/Behavioral Disorder'),
            ('GD','Global Delay'),
            ('LD','Learning Delay'),
            ('PDD','Pervasive Developmental Disorder')])
    status = models.CharField(max_length=20)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=[
        ('M','Male'), ('F','Female')])
    # One-to-many relationship to Evaluation in definition of Evaluation

    # Name to be displayed in admin
    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)


class Evaluator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    # Name to be displayed in admin
    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Evaluator, on_delete=models.CASCADE)
    createdAt = models.DateField()
    editedAt = models.DateField()
    notesSection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.notes_blank)
    reflexSection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.reflex_blank)
    tactilitySection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.tactility_blank)
    auditorySection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.auditory_blank)
    visualSection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.visual_blank)
    manualSection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.manual_blank)
    languageSection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.language_blank)
    mobilitySection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.mobility_blank)
    sensorySection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.sensory_blank)
    sensitivitiesSection = JSONField(encoder=DjangoJSONEncoder, \
            default=json_defaults.sensitivities_blank)
