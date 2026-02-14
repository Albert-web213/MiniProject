from django.urls import path
from Admin import views

app_name="Admin"

urlpatterns = [
   path('District/',views.District,name="District"),
   path('deletedistrict/<int:id>',views.deletedistrict,name="deletedistrict"),
   path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),

   path('Place/',views.Place,name="Place"),
   path('deleteplace/<int:id1>',views.deleteplace,name="deleteplace"),

   path('Subcategory/',views.Subcategory,name="Subcategory"),

   path('Category/',views.Category,name="Category"),
   path('Category/<int:id>',views.delete_Category,name="delete_category"),
   
   path('Admin_registration/',views.Admin_registration,name="Admin_registration")
]
