from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('completed-tasks/', views.completed_tasks, name="completed-tasks"),
    path('uncompleted-tasks/', views.uncompleted_tasks, name="uncompleted-tasks"),
  ]