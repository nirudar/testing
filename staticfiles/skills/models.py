from django.db import models

class Skills(models.Model):
     #skills.html
    skills_name=models.CharField(max_length=50)
    rating=models.PositiveIntegerField(max_length=10)
# Create your models here.
