from django.urls import path,include
from Guest import views
urlpatterns = [
   path('Login/',views.Login,name="Login"),
   path('UserRegistration/',views.UserRegistration,name="UserRegistration")
]
