
from django.urls import path,include
from User import views
urlpatterns = [
  path('MyProfile/',views.MyProfile,name="MyProfile")
]
