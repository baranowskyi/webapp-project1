from django.urls import path
from . import views

urlpatterns = [   
    path('<slug:slug_artist>/', views.main, name='main'),   
    path('<slug:slug_artist>/popular-tracks/', views.main, name='main'),    
    path('<slug:slug_artist>/tracks/', views.main, name='main'), 
    path('<slug:slug_artist>/albums/', views.main, name='main'), 
    path('<slug:slug_artist>/sets/', views.main, name='main'), 
    path('<slug:slug_artist>/reposts/', views.main, name='main'), 
     
]

