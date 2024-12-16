from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


#Cette vue permet de lister , creer , modifier une tache
def task_list(request):
    
    #affiche toutes les taches dans la base de donnees
    tasks = Task.objects.all()
    
    # Creation d'une tache
    if request.method == 'POST':
        if 'create_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task_list')
            
        # Mise a jour d'une tache 
        elif 'update_task' in request.POST:
            task = get_object_or_404(Task, pk=request.POST.get('task_id'))
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        
        # Suppression d'une tache
        elif 'delete_task' in request.POST:
            task = get_object_or_404(Task, pk=request.POST.get('task_id'))
            task.delete()
            return redirect('task_list')
        
        # cela permet de marquer une tache comme finie
        elif 'complete_task' in request.POST:
            task = get_object_or_404(Task, pk=request.POST.get('task_id'))
            task.completed = True
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todoapp/menu.html', {'form': form ,'tasks': tasks})