from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),    
    path('<slug:slug_artist>/', views.profile, name='profile'),  
]

