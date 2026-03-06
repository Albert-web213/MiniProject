from django.urls import path,include
from CivilEngineer import views

app_name='CivilEngineer'
urlpatterns = [
  path('MyProfile/',views.MyProfile,name="MyProfile"),
  path('Editprofile/',views.Editprofile,name="Editprofile"),
  path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
  path('Homepage/',views.Homepage,name="Homepage"),
  path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
  path('Reply/<int:id>',views.Reply,name="Reply")
]

