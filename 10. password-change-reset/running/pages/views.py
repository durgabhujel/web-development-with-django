from django.shortcuts import render

from django.views.generic import TemplateView #new

class HomePageView(TemplateView):
    template_name = 'home.html'

class HomePageView(TemplateView):
    template_name = 'home.html'  #new


class ContactPageView(TemplateView):
    template_name = 'contact.html'  #new

class AboutPageView(TemplateView):
    template_name = 'about.html'    
class skillPageView(TemplateView):
    template_name = 'skill.html'

