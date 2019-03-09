from django.contrib import admin
from .models import Student
from .models import Evaluation
from .models import Evaluator

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    pass

@admin.register(Evaluator)
class EvaluatorAdmin(admin.ModelAdmin):
    pass
