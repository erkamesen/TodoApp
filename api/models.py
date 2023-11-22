from django.db import models
from django.utils import timezone

# Create your models here.

PRIORITIES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

class Tasks(models.Model):
    
    task = models.CharField(max_length=400, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='Medium')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = "tasks"
        ordering = ["-created_at"]

