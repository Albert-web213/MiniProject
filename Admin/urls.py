from django.urls import path
#import 
from Admin import views

app_name="Admin"

urlpatterns = [
   path('Homepage/',views.Homepage,name="Homepage"),

   path('District/',views.District,name="District"),
   path('deletedistrict/<int:id>',views.deletedistrict,name="deletedistrict"),
   path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),

   path('Place/',views.Place,name="Place"),
   path('deleteplace/<int:id1>',views.deleteplace,name="deleteplace"),
   path('editplace/<int:id>',views.editplace,name="editplace"),

   path('Subcategory/',views.Subcategory,name="Subcategory"),

   path('Category/',views.Category,name="Category"),
   path('delete_category/<int:id>',views.delete_Category,name="delete_category"),
   path('editCategory/<int:id>',views.editCategory,name="editCategory"),


   path('Admin_registration/',views.Admin_registration,name="Admin_registration"),


   path('CivilEngineerVerification/',views.CivilEngineerVerification,name="CivilEngineerVerification"),
   path('verify/<int:aid>',views.verify,name="verify"),
   path('reject/<int:rid>',views.reject,name="reject")
]
