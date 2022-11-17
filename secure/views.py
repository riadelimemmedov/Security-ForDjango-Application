from django.shortcuts import render,redirect
from django.contrib.auth.models import auth #or => from django.contrib.auth import login,logout,authentication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *


# Create your views here.

#!homeView
def homeView(request):
    context = {
        'home':'homeView'
    }   
    return render(request,'secure/home.html',context)

#!dashboardView
@login_required(login_url='two_factor:login')
def dashboardView(request):
    context = {
        'dashboard':'dashboardView'
    }   
    return render(request,'secure/dashboard.html',context)

#!registerView
def registerView(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Created user successfully')
            return redirect('two_factor:login')
        else:
            if form.cleaned_data.get('captcha') == None:
                form.add_error(None,'Please check captcha')
    context = {
        'form':form
    }   
    return render(request,'secure/register.html',context)


#!logoutView
@login_required(login_url='two_factor:login')
def logoutView(request):
    auth.logout(request)
    messages.add_message(request,messages.SUCCESS,'Logout successfully')
    return redirect('secure:homeView')#or LOGOUT_REDIRECT_URL defined at setting.py file


#!accountLockView
def accountLockView(request):
    context = {
        
    }
    return render(request,'secure/account-locked.html',context)

#pipenv --venv => go to inside virtual environment file
#python manage.py axes_reset => reset axes,used only development server.If not wait a number of time.Unclock your account
#python manage.py check --deploy => check issues,if issues show user command line interface
#python manage.py makemigrations --check => it only checks whether the migration files were created.
#python manage.py makemigrations --check --dry-run => If you don't want to create the migrations, combine it with --dry-run.Only show pending migrations showing terminal track







