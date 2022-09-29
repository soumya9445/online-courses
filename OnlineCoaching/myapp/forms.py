from cProfile import label
from enum import unique
from pyexpat import model
#from typing_extensions import Self
from django import forms
from myapp.models import Admin,StudentModel

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=['id','course','fees','faculty','image']

        def clean_fees(self,request):
            fees=self.clean_data['fees']
            if fees >= 5000 or fees <=15000:
                return fees
            else:
                raise forms.ValidationError('Invalid Amount')



        def clean_faculty(self,request):
            faculty=self.clean_data['faculty']            
            if faculty.is_alpha():
                return faculty
            else:
                raise forms.ValidationError('Faculty Name Must Be Character')    
            

class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=70,label='Student Name')
    contactno=forms.IntegerField(label='Student Contact')
    emailid=forms.EmailField(label='Student Emailid')
    address=forms.Textarea()
    gen=(('male','MALE'),('female','FEMALE'),('others','OTHERS'))
    gender=forms.ChoiceField(label='Student Gender',widget=forms.RadioSelect,choices=gen)
    class Meta:
        model=StudentModel
        fields=['id','name','contactno','emailid','address','gender']

    def clean_name(self):
        name=self.cleaned_data['name']
        if name.isalpha():
            return name
        else:
            raise forms.ValidationError('Name Must Be Character!!')      

    def clean_contactno(self):
        contactno=self.cleaned_data['contactno']
        if len(str(contactno))==10:
            return contactno

        else:
            raise forms.ValidationError('Contact Number Must Have 10 Digit!!')              

