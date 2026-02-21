from django.shortcuts import render,redirect 
#import
from Admin.models import *
from Guest.models import *
# Create your views here.

def Homepage(request):
    return render(request,"Admin/Homepage.html")

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
        name=request.POST.get('txt_category')
        editdata.category_name=name
        editdata.save()
        return redirect('Admin:Category')
    else:
        return render(request,"Admin/Category.html",{"editdata":editdata})



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
    districtData=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=='POST':
            #the name('District') is the value name used in select tag of dropdown
            District_id=tbl_district.objects.get(id=request.POST.get('sel_district'))
            place=request.POST.get('txt_place')
            #the names used is same in both views and models
            tbl_place.objects.create(district=District_id,place=place)
            return redirect('Admin:Place')
    else:   
        return render(request,"Admin/Place.html",{"place":place,'districtData':districtData})

def deleteplace(request,id1):
    tbl_place.objects.get(id=id1).delete()
    return redirect('Admin:Place')

def editplace(request,id):
    editdata=tbl_place.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('txt_place')
        editdata.place=name
        editdata.save()
        return redirect('Admin:Place')
    else:
         return render(request,"Admin/Place.html",{"editdata":editdata})



def Subcategory(request):
    categorydata=tbl_category.objects.all()
    if request.method=='POST':
        #dropdown ,so we use the foreign key concept,id is taken and value as stored and itself stored in category_id
        category_id = tbl_category.objects.get(id= request.POST.get("sel_category"))
        subcategoryname = request.POST.get("txt_Sub")
        tbl_subcategory.objects.create(category=category_id,subcategory_name=subcategoryname)
        return redirect('Admin:Subcategory')
    else:
        return render(request,"Admin/Subcategory.html",{"categorydata":categorydata})
    

def CivilEngineerVerification(request):
    civilengineerdata=tbl_civilengineering.objects.all()
    return render(request,"Admin/CivilEngineerVerification.html",{"civilengineerdata":civilengineerdata})


def verify(request,aid):
    civileng= tbl_civilengineering.objects.get(id=aid)
    civileng.civileng_status = 1
    civileng.save()
    return redirect("Admin:CivilEngineerVerification")

def reject(request,rid):
    civileng=tbl_civilengineering.objects.get(id=rid)
    civileng.civileng_status=2
    civileng.save()
    return redirect("Admin:CivilEngineerVerification")