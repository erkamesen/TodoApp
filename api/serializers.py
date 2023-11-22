from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    elapsed_time_seconds = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = '__all__'

    def get_elapsed_time_seconds(self, obj):

        now = timezone.now()
        elapsed = now - obj.created_at
        return elapsed.total_seconds()

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

