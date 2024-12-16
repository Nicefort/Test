from django import forms
from .models import Task


# Cretion de la formulaire avec les champs necessaire pour utitiliser dans les gabarits (html)
class TaskForm(forms.ModelForm):
       class Meta:
           model = Task
           fields = ['title', 'description', 'completed', 'due_date', 'priority']
           widgets = {
               'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
           }