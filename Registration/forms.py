from django import forms
from .models import Employee


class EmployeeForm(forms.Form):
    choices_gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    empId = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_NO = forms.CharField(max_length=15)
    dateOfBirth = forms.DateField()
    gender = forms.ChoiceField(choices=choices_gender)
    aadharNo = forms.CharField(max_length=50)
    aadhar_Image = forms.FileField()
    panCard_Image = forms.FileField()
    profile_pic = forms.FileField()

    class Meta:
        model = Employee
        fields = ('empId','name','email','phone_NO','dateOfBirth','gender',
                  'aadharNo','aadhar_Image','panCard_Image','profile_pic')
