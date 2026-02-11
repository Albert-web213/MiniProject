from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.


def Admin_registration(request):
    Admin_registration=tbl_admin.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt1_name')
        email=request.POST.get('txt_mail')
        password=request.POST.get('Password')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,"Admin/Admin_registration.html")
    else:
        return render(request,"Admin/Admin_registration.html",{'Admin':Admin_registration})

def Category(request):
    category = tbl_category.objects.all()
    if request.method=='POST':
        name1=request.POST.get('txt_category')
        tbl_category.objects.create(category_name=name1)
        return render(request,"Admin/Category.html")
    else:
        return render(request,"Admin/Category.html")

def District(request):
    district = tbl_district.objects.all()
    # button click
    if request.method=='POST':
        name=request.POST.get('txt_name')
        #insert qry -->
        tbl_district.objects.create(district_name=name)
        return render(request,"Admin/District.html")
    else:
        return render(request,"Admin/District.html",{"district":district})
    
def deletedistrict(request, id):
    tbl_district.objects.get(id=id).delete()
    return redirect('Admin:District')

def Place(request):
    return render(request,"Admin/Place.html")

def Subcategory(request):
    return render(request,"Admin/Subcategory.html")