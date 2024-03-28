from django.contrib import admin
from skills.models import Skills

class SkillsAdmin(admin.ModelAdmin):
    list_display=('skills_name','rating')
    
admin.site.register(Skills,SkillsAdmin)
# Register your models here.
