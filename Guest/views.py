from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
# Create your views here.

def Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("Password")
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()

        if admincount > 0:
            admindata = tbl_admin.objects.get(admin_email=email,admin_password=password)
            #login cheyyuna persons data is stored in session
            request.session['aid'] = admindata.id
            return redirect("Admin:Homepage")
        elif usercount > 0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect("User:Homepage")
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid Email Or Password"})
    return render(request,"Guest/Login.html")

def UserRegistration(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('Address')
        photo=request.FILES.get('file')
        place=tbl_place.objects.get(id=request.POST.get('Place'))
        password=request.POST.get('Password')
        tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_photo=photo,place=place,user_password=password)
        return render(request,"Guest/UserRegistration.html")
    else:
        return render(request,"Guest/UserRegistration.html",{"district":district})
    
def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get("did"))
    place=tbl_place.objects.filter(district=districtid)
    #melilulla place
    return render(request,"Guest/AjaxPlace.html",{"place":place})

def CivilEngineering(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('Address')
        photo=request.FILES.get('file')
        proof=request.FILES.get('file')
        place=tbl_place.objects.get(id=request.POST.get('Place'))
        password=request.POST.get('Password')
        tbl_civilengineering.objects.create(civileng_name=name,civileng_email=email,civileng_contact=contact,civileng_address=address,civileng_photo=photo,civileng_proof=proof,place_id=place,civileng_password=password)
        return render(request,"Guest/CivilEngineering.html")
    else:
        return render(request,"Guest/CivilEngineering.html",{"district":district})
    

def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get("did"))
    place_id=tbl_place.objects.filter(district=districtid)
    #melilulla place
    return render(request,"Guest/AjaxPlace.html",{"place":place_id})