from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'github_link')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'tools_used')
