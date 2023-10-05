from django.contrib import admin

from todoapp.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("tags__name",)
    list_display = (
        "content",
        "created_at",
    )


admin.site.register(Tag)
