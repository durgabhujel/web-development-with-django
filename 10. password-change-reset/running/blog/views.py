from django.shortcuts import render

from django.views.generic.edit import CreateView ,UpdateView,DeleteView# new
from .forms import BlogForm
from django.urls import reverse_lazy # new

from .models import Blog

#function based view
def blogs(request):
    context = {
        'blogs': Blog.objects.all()  # Blog.objects.all() is a QuerySet object (list of objects) from the Blog model (Blog.objects.all() is a list of Blog objects)
    }
    return render(request, 'blogs/blogs.html', context)

def blog_detail(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_detail.html', context)    


class BlogCreateView(CreateView): # new
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/blog_create.html'
    #fields = ['title','subtitle', 'author', 'body']  #or fields = '__all__'

class BlogUpdateView(UpdateView): # new
    model = Blog
    #form_class = BlogForm
    template_name = 'blogs/blog_edit.html'
    fields = ['title','subtitle', 'body','header_image']      

class BlogDeleteView(DeleteView): # new
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blogs')     