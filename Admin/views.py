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
        return render(request,"Admin/Category.html",{"category":category})
    
def delete_Category(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect('Admin:Category')

def editCategory(request,id):
    editdata=tbl_category.objects.get(id=id)
    if request.method=='POST':
        name1=request.POST.get()

def District(request):
    district = tbl_district.objects.all()
    # button click
    if request.method=='POST':
        name=request.POST.get('txt_name')
        #insert qry -->
        tbl_district.objects.create(district_name=name)
        return redirect('Admin:District')
    else:
        return render(request,"Admin/District.html",{"district":district})
    
def deletedistrict(request, id):
    tbl_district.objects.get(id=id).delete()
    return redirect('Admin:District')

def editdistrict(request, id):
    editdata=tbl_district.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('txt_name')
        editdata.district_name=name
        editdata.save()
        return redirect('Admin:District')
    else:
        return render(request,"Admin/District.html",{'editdata':editdata})

def Place(request):
    place=tbl_place.objects.all()
    if request.method=='POST':
            name=request.POST.get('District')
            place=request.POST.get('txt_place')
            tbl_place.objects.create(district_name=name,place_name=place)
            return render(request,"Admin/Place.html")
    else:   
        return render(request,"Admin/Place.html",{"place":place})

def deleteplace(request,id1):
    tbl_place.objects.get(id=id1).delete()
    return redirect('Admin:Place')

def Subcategory(request):
    return render(request,"Admin/Subcategory.html")