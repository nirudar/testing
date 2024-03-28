from django.contrib import admin
from education.models import Education

class EducationAdmin(admin.ModelAdmin):
    list_display=('course','university','college_address','course_start_date','course_end_date',
                  'course_description')
    
admin.site.register(Education,EducationAdmin)

# Register your models here.
