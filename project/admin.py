from django.contrib import admin
from project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display=('project_name','project_role','project_description')

admin.site.register(Project,ProjectAdmin)

# Register your models here.
