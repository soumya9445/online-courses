from datetime import datetime
from django.db import models

# Create your models here.
class Admin(models.Model):
    courses=(
        ('python','python'),
        ('django','django'),
        ('restapi','restapi')
    )
    #name=models.CharField(max_length=100)
    course=models.CharField(choices=courses,max_length=100)
    fees=models.FloatField()
    faculty=models.CharField(max_length=50)
    image=models.ImageField(upload_to='faculty_images/',default=False,blank=True)
    #time=models.DateTimeField()

class StudentModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    contactno=models.IntegerField(unique=True)
    emailid=models.EmailField()
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)    