from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,FormView
from myapp.forms import AdminForm,StudentForm
from myapp.models import Admin,StudentModel
from django.contrib.messages.views import SuccessMessageMixin

def show(request):
    return render(request,'show.html')

def institute(request):
    return render(request,'institute.html')

def admin_part(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request,'Login Successfully!!')
                    return redirect('profile')   

    else:
        fm=AuthenticationForm()
    return render(request,'admin.html',{'form1':fm})

class profile(CreateView,SuccessMessageMixin):
    template_name='profile.html'
    model=Admin
    fields="__all__"
    #form_class=AdminForm
    success_url='/profile/'
    success_message='Insert Record Is Successfully!!'

class View(ListView):
    template_name='view.html'
    model=Admin

class Update(UpdateView,SuccessMessageMixin):
    template_name='update.html'
    fields='__all__'
    model=Admin
    success_url='/view_page/'
    success_message='update successfull!!'    

class Delete(DeleteView,SuccessMessageMixin):
    template_name='delete.html'
    model=Admin
    success_url='/view_page/'

def register(request):
    result=StudentForm()
    return render(request,'register.html',{'form':result})   

def save_stu(request):
    if request.method == 'POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Registration Successfully!!')
            return redirect('save_stu')

    else:
        fm=StudentForm()
    return render(request,'register.html',{'form':fm})  

def student_login(request):
    return render(request,'login.html')   

def validate(request):
    na=request.POST.get('name')
    em=request.POST.get('emailid')
    try:
        result=StudentModel.objects.get(name=na,emailid=em)
        return redirect('courses')

    except StudentModel.DoesNotExist:
        messages.error(request,'Invalid User')
        return redirect('student_login') 

def courses(request):
    return render(request,'courses.html')        

def click(request):
    messages.success(request,'Register Successfuuly')
    return render(request,'click.html')    


        
    


                     





                     