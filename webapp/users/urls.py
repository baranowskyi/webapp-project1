#from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [    
    path('users/reg/', views.RegistrationView.as_view(), name='reg'),    
    path('users/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
]