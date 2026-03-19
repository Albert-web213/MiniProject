from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns = [
   path('Login/',views.Login,name="Login"),
   path('UserRegistration/',views.UserRegistration,name="UserRegistration"),
   path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
   path('CivilEngineering/',views.CivilEngineering,name="CivilEngineering"),
   path('index/',views.index,name="index"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('otp/',views.otp,name="otp"),
    path('newpass/',views.newpass,name="newpass"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
]
