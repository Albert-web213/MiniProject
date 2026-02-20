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
    if request.method=='POST':
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('retype_password')
        old_password=request.POST.get('old_password')
        user = tbl_user.objects.get(id=request.session['uid'])
        if user.user_password==old_password:
            if new_password==confirm_password: 
                user.user_password=confirm_password 
                user.save()
            else:
                return render(request,"User/ChangePassword.html",{'msg':"Invlaid password"})
        else:   
            return render(request,"User/ChangePassword.html",{'msg':"Old password has error"})
    return render(request,"User/ChangePassword.html")

def Homepage(request):
    return render(request,"User/Homepage.html")


