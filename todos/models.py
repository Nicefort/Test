from django.db import models
from django.utils import timezone


#Creation du model pour la base de données (c'est comme creer la table Task )
class Task(models.Model):
       PRIORITY_CHOICES = [
           ('low', 'Low'),
           ('medium', 'Medium'),
           ('high', 'High'),
       ]

       title = models.CharField(max_length=200)
       description = models.TextField(blank=True)
       completed = models.BooleanField(default=False)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       due_date = models.DateTimeField(null=True, blank=True)
       priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')

        #Fonction qui permet de determiner si la durée de fin d'une tache est deja depassée ou non 
       def is_overdue(self):
           if self.due_date and timezone.now() > self.due_date:
               return True
           return False

       def __str__(self):
           return self.title