from django.urls import path
from . import views

urlpatterns = [
    path('profiles/<int:user_id>/', views.profileview, name='profile'),  # Fixed: added int converter and trailing slash
    path('list/', views.listusers, name='list_users'),
    path('marvel/', views.marvel, name='marvel')
]
 