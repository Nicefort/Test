from django.urls import path
from . import views


urlpatterns = [
        #Lien vers la page html 
       path('', views.task_list, name='task_list'),
   ]