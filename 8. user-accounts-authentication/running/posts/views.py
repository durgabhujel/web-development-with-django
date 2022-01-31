'''from django.shortcuts import render

from .models import Post

#function based view
def posts(request):
    context = {
        'posts': Post.objects.all()  # Post.objects.all() is a QuerySet object (list of objects) from the Post model (Post.objects.all() is a list of Post objects)
    }
    return render(request, 'posts/posts.html', context)
'''