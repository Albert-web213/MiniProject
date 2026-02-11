from django.urls import path
from Admin import views
urlpatterns = [
   path('District/',views.District,name="District"),
   path('Place/',views.Place,name="Place"),
   path('Subcategory/',views.Subcategory,name="Subcategory"),
   path('Category/',views.Category,name="Category"),
   path('Admin_registration/',views.Admin_registration,name="Admin_registration")
]
