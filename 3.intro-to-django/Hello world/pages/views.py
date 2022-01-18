from django.shortcuts import render

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')

def aboutPageView(request):
    return HttpResponse('Hello this is about pages')

def contactPageView(request):
    return HttpResponse('Hello this is contact page')    

def projectView(request):
    return HttpResponse('hello this is project page')       