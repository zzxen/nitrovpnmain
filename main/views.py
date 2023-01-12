from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News , Updates , Service

# Create your views here.

@login_required
def homepage(request):
    return render(request , "index.html")

def registerform(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("successmsg")

        else:
            messages.error(request , "Login Failed. Use another username")
            
    else:
        form = forms.RegisterForm()
    return render(request , "register.html" , {'form' : form})

def loginform(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"] , password = form.cleaned_data["password"])

            if user is not None:
                if user.is_active:
                    login(request , user)
                    return redirect("home")
                else:
                    return redirect("404error")
        else:
            messages.error(request , "Login failed. Username or Password incroccet")
    else:
        form = forms.LoginForm()
    
    return render(request , "login.html" , {'form' : form})

def error404(request):
    return render(request , "error-404.html")

def error505(request):
    return render(request , "error-500.html")

def successmsg(request):
    return render(request , "success.html")

def logoutform(request):
    logout(request)
    return redirect("signin")

def newsform(request):
    updatess = Updates.objects.all()
    newss = News.objects.all()
    return render(request , "news.html" , context = {"updates" : updatess , "news" : newss})

def serviceform(request):
    services = Service.objects.all()
    return render(request , "service.html" , context = {"service" : services})