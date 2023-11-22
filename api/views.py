from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Tasks
from rest_framework import status

# API DASHBOARD
@api_view(['GET'])
def api_dashboard(request):
    api_urls = {
        'List' : '/tasks/',                             # READ
        'Detail View' : '/task-detail/<str:id>/',       # READ
        'Create' : '/task-create/',                     # CREATE
        'Update' : '/task-update/<str:id>/',            # UPDATE
        'Delete' : '/task-delete/<str:id>/',            # DELETE
    }
    return Response(api_urls)

@api_view(["GET"])
def get_tasks(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_task(request, id):
    task = Tasks.objects.filter(id=id).first()

    if not task:
        return Response({
            "status" : "failure",
            "message": "Task is not found."
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def update_task(request, pk):
    task = Tasks.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)