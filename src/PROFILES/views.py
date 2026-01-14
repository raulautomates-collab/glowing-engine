from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

# user permissions view
@login_required  # checking if user is logged in
def profileview(request, user_id=None):
    user=request.user
    

    profile_user_obj = get_object_or_404(User, pk=user_id)
    
    context = {
        'username': profile_user_obj.username,
        'profile_user_obj': profile_user_obj
    }

    return render(request, 'profile.html', context)

# user list view
def listusers(request):
    myusers = User.objects.all()
    activesusers = User.objects.filter(is_active=True)
    context = {
        'myusers': myusers,
    }
    return render(request, 'listingpage.html', context)
    

def marvel(request):
    return render(request, 'marvel.html')