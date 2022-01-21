from django.shortcuts import render


from .models import Blog

#function based view
def blogs(request):
    context = {
        'blogs': Blog.objects.all()  # Blog.objects.all() is a QuerySet object (list of objects) from the Blog model (Blog.objects.all() is a list of Blog objects)
    }
    return render(request, 'blogs/blogs.html', context)
