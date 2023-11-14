from django.shortcuts import render,redirect
from lms_app.models import Cls
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from account.models import Account
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

# The main page
def main(request):
    return render(request,'lms_app/main.html')


def classes(request):
    course_classes = Cls.objects.all()

    lenth = course_classes.__len__()
    course_classes = Cls.objects.order_by('started_date')

    # search functionality
    name = request.GET.get('search')
    if name != '' and name is not None:
        course_classes = course_classes.filter(name__icontains=name)

    # Pagination
    paginator = Paginator(course_classes,10)
    page = request.GET.get('page')
    course_classes = paginator.get_page(page)


    return render(request,'lms_app/classes.html',{"course_classes":course_classes,'len':lenth})


# Detail view
def detail(request,class_id):
    cls_id = Cls.objects.get(id=class_id)
    std = Account.objects.all()
    class_obj = Account.objects.filter(cls__id= class_id)

    context = {
        'class_id':cls_id,
        'std':std,
        'class_obj':class_obj,
        }   
    return render(request,'lms_app/detail.html',context)



# create view
def create(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST['name']    
        t = request.POST['time']    
        d = request.POST['date']
        try:
            clas=Cls.objects.create(name=n,time=t,started_date=d)
            clas.save()
            error = 'no'
        except:
            error = 'yes'

    return render(request,'lms_app/create.html',{'error':error})


# delete view
def delete(request,class_id):
    cls = Cls.objects.get(id=class_id)
    cls.delete()
    messages.error(request,cls.name + ' Is successfully deleted')
    return redirect('classes')


# update view
def update(request,class_id):
    clas = Cls.objects.get(id=class_id)
    if request.method == 'GET':
        return render(request,'lms_app/update.html',{'clas':clas})
    else:
        name = request.POST.get('name')    
        time = request.POST.get('time')    
        started = request.POST.get('date') 

        clas.name = name   
        clas.time = time   
        clas.started_date = started
        clas.save()
        messages.success(request,clas.name + ' updated')
        return redirect('classes')


def userInfo(request,user_id):
    user_obj = Account.objects.get(id=user_id)
    return render(request,'lms_app/userInfo.html',{'user_obj':user_obj})



# Register user
def register(request):
    if request.method == 'GET':
        return render(request,'lms_app/register.html')
    else:
        nam = request.POST.get('name')       
        email = request.POST.get('email')       
        password = request.POST.get('password')       
        conf_password = request.POST.get('conf_password') 
        add = request.POST.get('address') 

        # 1st Check
        if password != conf_password:
            messages.error(request,'Password didn\'t much.')
            return redirect('register')

        # 2nd Check
        exist = Account.objects.filter(email=email).exists()

        if exist:
            messages.error(request,'Email already exist.')
            return redirect('register')


        user  = Account.objects.create_user(name=nam,email=email,password=password,address=add)
        messages.success(request,nam + ' User created ')
        return redirect('main')

            

        

# login functionallity
def Login(request):
    if request.method == 'POST':
        u = request.POST['usrnam']
        p = request.POST['paswrd']
        
        user = authenticate(username= u, password= p)
        
        login(request,user)
        messages.success(request,'User logged in')
        return redirect('main')
    return render(request,'lms_app/login.html') 


# logout functionallity
def logut(request):
    logout(request)
    messages.success(request,'User logged out')
    return redirect('main')


# User information
def user(request):
    usr = Account.objects.all()  
    return render(request,'lms_app/user.html',{"usr":usr})



# Enrollment
def enrollment(request):
    account = Account.objects.all()
    class_object = Cls.objects.all()
    error = ""

    if request.method == 'POST':

        try:
            cl = request.POST['clas']
            us = request.POST['user']
            em = request.POST['email']
            c1 = Cls.objects.get(name=cl)
            c1.save()
            u1 = Account.objects.get(name=us,email=em)
            u1.save()
            c1.students.add(u1)
            error = 'no'
            
        except:    
            error = 'yes'

    context={
        'class_object':class_object,
        'account':account,
        'error':error,
    }

    return render(request,'lms_app/enrollment.html',context)

