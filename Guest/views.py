from django.shortcuts import render

# Create your views here.

def Login(request):
    return render(request,"Guest/Login.html")

def UserRegistration(request):
    return render(request,"Guest/UserRegistration.html")