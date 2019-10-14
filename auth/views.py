from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from auth import forms

# Create your views here.

def Login(request):
    if request.method == "POST":
        form = request.POST.copy()
        username = form.get("UserName")
        password = form.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, 'Home/homepage.html')

        else:
            error = "Incorrect Username or Password"
            form = forms.LoginForm()
            return render(request, 'auth/login.html', {'error' : error, "form" : form})


    else:
        form = forms.LoginForm()
    return render(request, 'auth/login.html', { "form" : form })

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_protect
def CreateUser(request):
    if request.method == "POST":
        form = request.POST.copy()
        FirstName = form.get("FirstName")
        LastName = form.get("LastName")
        username = form.get("UserName")
        Mail = form.get("Email")
        password = form.get("password")

        user = authenticate(request, username = username, password = password)

        if user is None:
            user = User.objects.create_user(username, Mail, password)
            user.last_name = LastName
            user.first_name = FirstName
            user.save()
            return render(request, 'Home/homepage.html')


    else:
        form = forms.CreateUser()
    return render(request, 'auth/login.html', { "form" : form })
