from django.contrib import admin

from .models import Tasks


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "is_complete", "created_at", "priority")
    list_filter     = ("task", "created_at", "priority")
    search_fields   = ("task", )


