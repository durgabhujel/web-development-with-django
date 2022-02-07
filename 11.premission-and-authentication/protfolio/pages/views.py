from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView #new
from.models import homepage



#class HomePageView(TemplateView):
    #template_name = 'home.html'

def home_page(request):
    context={
        'pages': homepage.objects.first()
    }
    print(context)
    return render(request,'home.html',context)  



class AboutPageView(TemplateView):
    template_name = 'about.html' 
