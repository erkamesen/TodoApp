from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    resp = requests.get("http://127.0.0.1:8000/api/tasks/")
    tasks = json.loads(resp.content)
    context = {
        "tasks": tasks,
    }
    return render(request, "index.html", context=context)

def completed_tasks(request):
    resp = requests.get("http://127.0.0.1:8000/api/tasks/")
    tasks = json.loads(resp.content)
    completed_tasks = [task for task in tasks if task.get("is_complete")]
    context = {
        "tasks": completed_tasks,
    }
    return render(request, "completed.html", context=context)

def uncompleted_tasks(request):
    resp = requests.get("http://127.0.0.1:8000/api/tasks/")
    tasks = json.loads(resp.content)
    uncompleted_tasks = [task for task in tasks if not task.get("is_complete")]
    context = {
        "tasks": uncompleted_tasks,
    }
    return render(request, "uncompleted.html", context=context)






