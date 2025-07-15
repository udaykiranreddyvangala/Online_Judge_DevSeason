from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

def register_user(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request,'User with username already exits')
            return redirect("/auth/register")
        
        user=User.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        messages.info(request,'User created successfully')
        return redirect('/auth/login/')
    
    template=loader.get_template('register.html')
    context={}
    return HttpResponse(template.render(context,request))
        
def login_user(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        
        if not user.exists():
            messages.info(request,"User with this username does not exist")
            return redirect('/auth/register/')

        user=authenticate(username=username,password=password)
        
        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/login/')
        
        login(request,user)
        messages.info(request,'login successful')
        return redirect('/home/')
    
    template=loader.get_template('login.html')
    context={}
    return HttpResponse(template.render(context,request))

def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')