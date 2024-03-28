from django.db import models

class Education(models.Model):
      #Education.html
    course=models.TextField(max_length=100)
    university=models.TextField(max_length=250)
    college_address=models.TextField(max_length=250)
    course_start_date=models.PositiveIntegerField(max_length=4)
    course_end_date=models.TextField(max_length=4)
    course_description=models.TextField(max_length=200)

# Create your models here.
