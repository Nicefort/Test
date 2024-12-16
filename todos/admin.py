from django.contrib import admin
from .models import Task

# Register your models here.


# permet a l'admin de tout faire depuis l'interface de l'administration proposée par django
@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('title','description','completed','created_at',)
    search_fields = ['title',] 
