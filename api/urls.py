from django.urls import path
from . import views


urlpatterns = [
    path('docs/', views.api_dashboard, name="api-dashboard"),
    path("tasks/", views.get_tasks, name="get-tasks"),
    path("task/<int:id>/", view=views.get_task, name="get-task"),
    path('task-update/<int:id>/', views.update_task, name="update-task"),
  ]