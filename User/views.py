from django.shortcuts import render,redirect
from Guest.models import*
from User.models import*
from django.http import JsonResponse
from .utils import GeminiDesignGenerator
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


def ViewsCivilEngineering(request):
    civilengdata=tbl_civilengineering.objects.filter(civileng_status = 1)
    return render(request,"User/ViewsCivilEngineering.html",{"civilengdata":civilengdata})
    

def Complaint(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    complaintdata=tbl_complaint.objects.all()
    if request.method=='POST':
        title=request.POST.get('txt_title')
        content=request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_title=title, complaint_content=content,user_id=userdata)
        return redirect("User:Complaint")
    else:
        return render(request,"User/Complaint.html",{"complaintdata":complaintdata})


def deletecomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect('User:Complaint')


def Request(request,cid):
    civildata=tbl_civilengineering.objects.get(id=cid)
    userdata=tbl_user.objects.get(id=request.session['uid'])
    request_data=tbl_request.objects.all()
    if request.method=="POST":
        planefile=request.FILES.get("file")
        Documentation=request.FILES.get("documentation")
        Description=request.POST.get("description")
        tbl_request.objects.create(request_plane_file=planefile,request_doc=Documentation,request_description=Description,user_id=userdata,civileng_id= civildata)
        return render(request,"User/Request.html")
        
    else:
        return render(request,"User/Request.html",{"request_data":request_data})

   

def MyRequest(request):
    requestdata=tbl_request.objects.all()
    return render(request,"User/MyRequest.html",{"requestdata":requestdata})


def deleterequest(request,id):
    tbl_request.objects.get(id=id).delete()
    return redirect('User:MyRequest')

def createplan(request):
    return render(request, "User/CreatePlan.html")


def generate_design(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed."}, status=405)

    data = {
        "width": request.POST.get("width"),
        "length": request.POST.get("length"),
        "sqft": request.POST.get("sqft"),
        "floors": int(request.POST.get("floors", 1)),
        "shape": request.POST.get("shape", "Rectangular"),
        "unit_type": request.POST.get("unit_type", "2BHK"),
        "bedrooms": request.POST.get("bedrooms", "2"),
        "bathrooms": request.POST.get("bathrooms", "2"),
        "style": request.POST.get("style", "Modern Premium"),
        "soil": request.POST.get("soil", "Firm"),
        "kitchen_type": request.POST.get("kitchen_type", "Open"),
        "budget": request.POST.get("budget", "Standard"),
        "entrance": request.POST.get("entrance", "Any"),
        "vastu": request.POST.get("vastu", "Yes"),
        "parking": request.POST.get("parking", "No"),
        "balcony": request.POST.get("balcony", "No"),
        "puja_room": request.POST.get("puja_room", "No"),
        "utility_area": request.POST.get("utility_area", "No"),
        "dining": request.POST.get("dining", "Yes"),
        "study_room": request.POST.get("study_room", "No"),
        "prefs": request.POST.get("prefs", "").strip(),
    }

    if not ((data["width"] and data["length"]) or data["sqft"]):
        return JsonResponse(
            {"error": "Please provide plot width and length, or total square footage."},
            status=400
        )

    try:
        generator = GeminiDesignGenerator()
        result = generator.generate_plan(data)

        if result:
            return JsonResponse(result)

        return JsonResponse(
            {"error": "AI could not generate the plan. Please check inputs or API configuration."},
            status=500
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)