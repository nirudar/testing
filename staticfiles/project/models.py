from django.db import models

class Project(models.Model):
     #project.html
    project_name=models.CharField(max_length=100)
    project_role=models.CharField(max_length=150)
    project_description=models.TextField(max_length=500)
    
    #image Project
    project_image=models.FileField(upload_to="project_image/",null=True,default=None,max_length=300)

# Create your models here.
