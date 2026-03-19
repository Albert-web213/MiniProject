
from django.urls import path,include
from User import views
app_name='User'
urlpatterns = [
  path('MyProfile/',views.MyProfile,name="MyProfile"),
  path('Editprofile/',views.Editprofile,name="Editprofile"),
  path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
  path('Homepage/',views.Homepage,name="Homepage"),
  path('ViewsCivilEngineering/',views.ViewsCivilEngineering,name="ViewsCivilEngineering"),
  path('Complaint/',views.Complaint,name="Complaint"),
  path('deletecomplaint/<int:id>',views.deletecomplaint,name="deletecomplaint"),
  path('Request/<int:cid>',views.Request,name="Request"),
  path('MyRequest/',views.MyRequest,name="MyRequest"),
  path('deleterequest/<int:id>',views.deleterequest,name="deleterequest"),

  path('createplan/', views.createplan, name='createplan'),
  path('generate_design/', views.generate_design, name='generate_design'),
]
