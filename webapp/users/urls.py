from django.urls import path

from users.views import *

urlpatterns = [ 

    #old 
    path('login/', login_user, name='login'),

    path('api/user/register/', RegisterUserView.as_view(), name='register_user'),
    path('api/user/login/', LoginUserView.as_view(), name='login_user'), 
    path('api/user/logout/', LogoutUserView.as_view(), name='logout_user'),
    path('api/user/me/', MeUserView.as_view(), name='get_current_user'),
    path('api/user/refresh-token/', RefreshJWTToken.as_view(), name='refresh_token_user'),
       
]