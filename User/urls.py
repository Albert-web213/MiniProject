
from django.urls import path,include
from User import views
app_name='User'
urlpatterns = [
  path('MyProfile/',views.MyProfile,name="MyProfile"),
  path('Editprofile/',views.Editprofile,name="Editprofile"),
  path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
  path('Homepage/',views.Homepage,name="Homepage"),
]
