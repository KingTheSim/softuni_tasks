from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from mysite.tasks.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks_list = Task.objects.all()
    contex = {'tasks_list': tasks_list}
    return render(request, 'tasks/index.html', contex)
