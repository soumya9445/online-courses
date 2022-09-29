from django.contrib import admin
from myapp.models import Admin,StudentModel

# Register your models here.
@admin.register(Admin)

class Admin(admin.ModelAdmin):
    list_display=['id','course','fees','faculty','image']

@admin.register(StudentModel)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','contactno','emailid','address','gender']
