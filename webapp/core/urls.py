from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]