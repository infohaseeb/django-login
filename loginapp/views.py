from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



#Develop by Haseeb Asghar
#https://www.linkedin.com/in/infohaseeb/
#https://github.com/infohaseeb

def LoginUser(request):
    if request.user.username=="":
        return render(request,"login.html")
    else:
        return HttpResponseRedirect("/homepage")

@login_required(login_url="/loginuser/")
def HomePage(request):
    return render(request, "home.html")

def clicklogin(request):
    if request.method!="POST":
        return HttpResponse("<h1> Methoid not allowed<h1>")
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user=authenticate(username=username,password=password)
        if user!=None:
            login(request,user)
            return HttpResponseRedirect('/homepage')
        else:
            messages.error(request, "Invalid Login")
            return HttpResponseRedirect('/loginuser')

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser")            