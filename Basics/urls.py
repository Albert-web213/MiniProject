from django.urls import path
from Basics import views
urlpatterns = [

    path('Sum/',views.Sum,name="Sum"),
    path('Calcualtor/',views.Calculator,name="Calculator"),
    path('Largest/',views.Largest,name="Largest"),
    path('Marklist/',views.Marklist,name="Marklist")
]
