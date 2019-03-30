from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
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

# Create an admin panel for User that contains Evaluator editing
class EvaluatorInline(admin.StackedInline):
    model = Evaluator
    can_delete = False
    verbose_name_plural = 'evaluator'

class UserAdmin(BaseUserAdmin):
    inlines = (EvaluatorInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

