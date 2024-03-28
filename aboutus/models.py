from django.db import models

class AboutUs(models.Model):

 #about.html
    phone=models.PositiveIntegerField(max_length=10)
    email=models.EmailField(max_length=70)
    Address=models.TextField(max_length=150)
    #profile.html
    linkedin=models.URLField(max_length=150)
    github=models.URLField(max_length=150)
    website=models.URLField(max_length=150)
    
    #Files Uploadation
    cv_file=models.FileField(upload_to="cv/",null=True,default=None,max_length=300)
    profile_image=models.FileField(upload_to="profile_img/",null=True,default=None,max_length=300)
    

# Create your models here.
