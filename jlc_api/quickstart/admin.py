from django.contrib import admin
from .models import Student
from .models import Evaluation

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    pass

