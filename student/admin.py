from django.contrib import admin
from .models import Student,Mark
# Register your models here.
@admin.register(Student)
class StudentModel(admin.ModelAdmin):
    list_display =['name','email']

@admin.register(Mark)
class MarkModel(admin.ModelAdmin):
    list_display =['student','physics','chemistry','math']
