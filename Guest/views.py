from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.



def index(request):
    return render(request,"Guest/index.html")



def Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("Password")
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        civilcount=tbl_civilengineering.objects.filter(civileng_email=email,civileng_password=password).count()
        if admincount > 0:
            admindata = tbl_admin.objects.get(admin_email=email,admin_password=password)
            #login cheyyuna persons data is stored in session
            request.session['aid'] = admindata.id
            return redirect("Admin:Homepage")
        elif usercount > 0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect("User:Homepage")
        elif civilcount > 0 :
            civildata=tbl_civilengineering.objects.get(civileng_email=email,civileng_password=password)
            request.session['cid']=civildata.id
            return redirect("CivilEngineer:Homepage")
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
        address=request.POST.get('txt_address')
        photo=request.FILES.get('photo')
        proof=request.FILES.get('txt_proof')
        place=tbl_place.objects.get(id=request.POST.get('Place'))
        password=request.POST.get('password')
        tbl_civilengineering.objects.create(civileng_name=name,civileng_email=email,civileng_contact=contact,civileng_address=address,civileng_photo=photo,civileng_proof=proof,place_id=place,civileng_password=password)
        return render(request,"Guest/CivilEngineering.html")
    else:
        return render(request,"Guest/CivilEngineering.html",{"district":district})
    

def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get("did"))
    place_id=tbl_place.objects.filter(district=districtid)
    #melilulla place_id
    return render(request,"Guest/AjaxPlace.html",{"place":place_id})

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")

        user = tbl_user.objects.filter(user_email=email).first()
        civil = tbl_civilengineering.objects.filter(civileng_email=email).first()

        if user:
            request.session["fid"] = user.id
            request.session["type"] = "user"
        elif civil:
            request.session["fid"] = civil.id
            request.session["type"] = "civil"
        else:
            return render(request, "Guest/ForgotPassword.html", {"msg": "Email not found!"})

        otp = random.randint(111111, 999999)
        request.session["otp"] = otp

        html_message = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="UTF-8">
            <title>Password Reset OTP</title>
            </head>
            <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

            <table width="100%" cellspacing="0" cellpadding="0" style="background-color:#f4f6f8; padding:20px;">
            <tr>
            <td align="center">

            <table width="400" cellspacing="0" cellpadding="0" style="background:#ffffff; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.08); overflow:hidden;">
                
            <tr>
            <td style="background:#4CAF50; padding:20px; text-align:center; color:#ffffff; font-size:22px; font-weight:bold;">
            BUILDORA
            </td>
            </tr>

            <tr>
            <td style="padding:25px; color:#333333; font-size:14px; line-height:1.6;">
            <p>Hello,</p>

            <p>We received a request to reset your password. Use the OTP below:</p>

            <div style="text-align:center; margin:25px 0;">
            <span style="display:inline-block; padding:15px 25px; font-size:24px; letter-spacing:3px; font-weight:bold; color:#4CAF50; border:2px dashed #4CAF50; border-radius:8px;">
            {otp}
            </span>
            </div>

            <p>This OTP is valid for a short time. Do not share it.</p>

            <p>If you didn’t request this, ignore this email.</p>

            <p>Thank you,<br><strong>BUILDORA Team</strong></p>
            </td>
            </tr>

            <tr>
            <td style="background:#f1f1f1; padding:15px; text-align:center; font-size:12px; color:#777;">
            © 2026 BUILDORA
            </td>
            </tr>

            </table>

            </td>
            </tr>
            </table>

            </body>
            </html>
            """

        send_mail(
            'Forgot Password OTP',
            "Your OTP is: " + str(otp),  # fallback (plain text)
            settings.EMAIL_HOST_USER,
            [email],
            html_message=html_message
        )


        return redirect("Guest:otp")

    return render(request, "Guest/ForgotPassword.html")

def otp(request):
    if request.method == "POST":
        inp_otp = request.POST.get("txt_otp")

        if "otp" in request.session and str(request.session["otp"]) == inp_otp:
            return redirect("Guest:newpass")
        else:
            return render(request, "Guest/OTP.html", {"msg": "Invalid OTP!"})

    return render(request, "Guest/OTP.html")


def newpass(request):
    if request.method == "POST":
        if request.POST.get("txt_new_pass") == request.POST.get("txt_con_pass"):

            if request.session.get("type") == "user":
                user = tbl_user.objects.get(id=request.session["fid"])
                user.user_password = request.POST.get("txt_con_pass")
                user.save()

            elif request.session.get("type") == "civil":
                civil = tbl_civilengineering.objects.get(id=request.session["fid"])
                civil.civileng_password = request.POST.get("txt_con_pass")
                civil.save()


            return render(request,"Guest/NewPassword.html",{"msg1":"Password Updated Sucessfully...."})

        else:
            return render(request,"Guest/NewPassword.html",{"msg":"Error in confirm password..!!!"})

    else:
        return render(request,"Guest/NewPassword.html")


def about(request):
    return render(request,"Guest/About.html")


def service(request):
    return render(request,"Guest/Service.html")