from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from Guest.models import*
from User.models import*
from CivilEngineer.models import*
# Create your views here.
def MyProfile(request):
    civildata= tbl_civilengineering.objects.get(id=request.session['cid'])
    return render(request,"CivilEngineer/MyProfile.html",{'civildata':civildata})

def Editprofile(request):
    civildata=tbl_civilengineering.objects.get(id=request.session['cid'])
    if request.method=='POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        civildata.civileng_name_name=name
        civildata.civileng_email_email=email
        civildata.civileng_contact_contact=contact
        civildata.civileng_address_address=address
        civildata.save()
        return redirect("CivilEngineer:Editprofile")
    else:
        return render(request,"CivilEngineer/Editprofile.html",{'civildata':civildata})


def ChangePassword(request):
    return render(request,"CivilEngineer/ChangePassword.html")

def Homepage(request):
    return render(request,"CivilEngineer/Homepage.html")


def ViewRequest(request):
    requestdata=tbl_request.objects.all()
    return  render(request,"CivilEngineer/ViewRequest.html",{"requestdata":requestdata})

def Reply(request,id):
    requestdata=tbl_request.objects.get(id=id)
    if request.method=="POST":
       reply=request.POST.get('reply')
       requestdata.request_reply=reply
       requestdata.request_status=1
       requestdata.save()
       return render(request,"CivilEngineer/Reply.html")
    else:
        return render(request,"CivilEngineer/Reply.html",{"requestdata":requestdata})
