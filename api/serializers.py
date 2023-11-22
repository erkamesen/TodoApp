from .models import Tasks
from rest_framework import serializers
from django.utils import timezone
class TaskSerializer(serializers.ModelSerializer):
    elapsed_time_seconds = serializers.SerializerMethodField()
    class Meta:
        model = Tasks
        fields = '__all__'
    def get_elapsed_time_seconds(self, obj):

        now = timezone.now()
        elapsed = now - obj.created_at
        return elapsed.total_seconds()