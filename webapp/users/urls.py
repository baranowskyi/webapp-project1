#from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [    
    path('users/reg/', views.RegistrationView.as_view(), name='reg'),
    path('users/me/', views.MeView.as_view(), name='me'),
    path('users/change-password/', views.ChangePasswordView.as_view(), name='change_password'),

]