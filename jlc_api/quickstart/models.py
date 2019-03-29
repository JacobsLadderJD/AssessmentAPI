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
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    # Currently stub - more to be added

    # Name to be displayed in admin
    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)

class Evaluation(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    evaluatorId = models.ForeignKey(Evaluator, on_delete=models.CASCADE)
    createdAt = models.DateField()
    editedAt = models.DateField()
    # Currently stub - more to be added

