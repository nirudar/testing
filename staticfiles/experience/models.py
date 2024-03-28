from django.db import models


class Experience(models.Model):
     #experience.html
    company_name=models.CharField(max_length=150)
    designation=models.CharField(max_length=100)
    job_start_date=models.CharField(max_length=10)
    job_end_date=models.CharField(max_length=10)
    job_responsibility=models.TextField(max_length=500)
# Create your models here.
