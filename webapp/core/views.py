from django.shortcuts import render
from users.models import UserSite 
from core.models import *

# from django.contrib.auth import get_user_model
#User = get_user_model()

def main(request, slug_artist):
    return render(request, 'main.html')
