from django.urls import path
from . import views


urlpatterns = [
    path(
        'docs/',                                # http://127.0.0.1:8000/api/docs/
        view=views.api_dashboard, 
        name="api-dashboard"
        ),
    path(
        "tasks/",                               # http://127.0.0.1:8000/api/tasks/
        view=views.get_tasks, 
        name="get-tasks"
        ),
    path(
        "task/<int:id>/",                       # http://127.0.0.1:8000/api/task/<int:id>/
        view=views.get_task, 
        name="get-task"
        ),
    path(
        'task-update/<int:id>/',                # http://127.0.0.1:8000/api/task-update/<int:id>/
        view=views.update_task, 
        name="update-task"
        ),
    path(
        'task-create/',                         # http://127.0.0.1:8000/api/task-create/
        view=views.create_task, 
        name="create-task"
        ),
    path(
        'task-delete/<int:id>/',                         # http://127.0.0.1:8000/api/task-delete/<int:id>/
        view=views.delete_task, 
        name="delete-task"
        ),
  ]