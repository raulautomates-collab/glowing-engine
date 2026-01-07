from django.urls import path
from .views import * # Added space after 'from'

urlpatterns = [  # Corrected spelling to 'urlpatterns'
    path('', home_page_view, name='homepage'),
    path('home/',view=index,name='indexpage'),
    path('about/',view=about,name='aboutpage')
]