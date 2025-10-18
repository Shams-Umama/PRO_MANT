from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.models import Project
from todolist.models import Task
from .models import ta_sk


@login_required
def add(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist =Task.objects.filter(project=project).get(pk=todolist_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        ta_sk.objects.create(project=project, todolist=todolist, name=name, description=description, created_by=request.user)

        return redirect(f'/projects/{project_id}/{todolist_id}/')

    return render(request, 'ta_sk/add.html')


@login_required
def detail(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Task.objects.filter(project=project).get(pk=todolist_id)
    task_detail = ta_sk.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.GET.get('is_done', '') == 'yes':
        task_detail.is_done = True
        task_detail.save()

    return render(request, 'ta_sk/detail.html', {
        'ta_sk': task_detail
    })


