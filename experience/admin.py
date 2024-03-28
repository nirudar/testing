from django.contrib import admin
from experience.models import Experience

class ExperienceAdmin(admin.ModelAdmin):
    list_display=('company_name','designation','job_start_date','job_end_date',
                  'job_responsibility')
    
admin.site.register(Experience,ExperienceAdmin)

# Register your models here.
