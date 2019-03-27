from django.db import models

# Create your models here.

#choices_Team=[('team1'),('team2'),('team3')]
class Employee(models.Model):
    choices_gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    empId = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_NO = models.CharField(max_length=15)
    dateOfBirth=models.DateField()
    gender=models.CharField(max_length=50,choices=choices_gender)
   # teamName=models.CharField(max_length=50,choices=choices_Team)
    aadharNo=models.CharField(max_length=50)
    aadhar_Image=models.ImageField(upload_to="document/images")
    panCard_Image=models.ImageField(upload_to="document/images")
    profile_pic=models.ImageField(upload_to="profile_pic/images")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(null=True)
    is_deleted = models.BooleanField(null=True)

    #address=models.ForeignKey()
