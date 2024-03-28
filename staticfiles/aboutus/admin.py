from django.contrib import admin
from aboutus.models import AboutUs

class AboutUsAdmin(admin.ModelAdmin):
    #aboutus.html
     list_display=('phone','email','Address','linkedin','github','website','cv_file','profile_image')
     
admin.site.register(AboutUs,AboutUsAdmin)

# Register your models here.
