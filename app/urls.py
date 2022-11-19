from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.RegisterUser, name = "UserRegister"),
    path('login/',views.Login, name = "login"), 
    path('dashboard/',views.Dashboard, name = "dasboard"),
    path('activate/<token>',views.verifyaccount , name="verify"),
    path('sendinvoice/', views.sendinvoice , name="sendinvoice"),
    path('createinvoice',views.createinvoice,name="createinvoice")
    
]