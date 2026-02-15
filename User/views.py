from django.shortcuts import render,redirect

# Create your views here.
def MyProfile(request):
    return render(request,"User/MyProfile.html")
