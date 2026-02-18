from django.shortcuts import render,redirect
from Guest.models import*
# Create your views here.
def MyProfile(request):
    userdata = tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'userdata':userdata})

def Editprofile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=='POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        userdata.user_name=name
        userdata.user_email=email
        userdata.user_contact=contact
        userdata.user_address=address
        userdata.save()
        return redirect("User:Editprofile")
    else:
        return render(request,"User/Editprofile.html",{'userdata':userdata})


def ChangePassword(request):
    return render(request,"User/ChangePassword.html")

def Homepage(request):
    return render(request,"User/Homepage.html")


