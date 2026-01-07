

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from.models import *
import pathlib



def home_page_view(request,*args,**kwargs):
    
    return render(request,'home.html')
def index(request):
    queryset=PageVisit.objects.all()
    try:
        percent=(queryset.count()*100.0/queryset.count())
    except:
        percent=0    
    html_template='base.html'
    page_title='basehtmlpage'
    context={
        'my_title':page_title,
        'page_visit_count':queryset.count(),
        'percent':percent
         
    }
    PageVisit.objects.create()
    return render(request,html_template,context)


    

def about(request):
    return render(request,'about.html') 
