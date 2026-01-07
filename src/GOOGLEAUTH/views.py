from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

#user register view
def register_view(request):
    
    return render(request,'register.html')