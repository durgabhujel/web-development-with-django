# Forms ( CRUD Operations )
## Create , Edit , Delete blog entries


### Create
1. Add a link to create new blog entry in the blogs.html page
```
#blogs/blogs.html
{% extends 'base.html' %}
{% block content %}
<div class="flex">    
  <h1 class="hero-title">
    My recent blogs
  </h1>
  <a href="{% url 'blog_create' %}" class="nav-links underline">Create a new blog</a>
</div>

  
  <div class="blogs">
    {% for blog in blogs %}
    <div class="blog-card">
    <div class="blog-card-text">
        <div>
          {% comment %} <h4 class="blog-card-title">{{ blog.id }}</h4> {% endcomment %}
          <h4 class="blog-card-title">{{ blog.title }}</h4>
          <p class="blog-card-subtitle">
            posted by <em>{{ blog.author }}</em> 
          </p>
          <p class="blog-card-para">
            {{ blog.subtitle }}
          </p>
        </div>
        <a href="{% url 'blog_detail' blog.id %}" class="blog-card-link">More about this blog ↗</a>
      </div>
    <hr class="line">
  </div>
  {% endfor %}
</div>
 
{% endblock content %}
```
2. Add some css for flex (add this at the end of the css file)
```
#css/base.css

.flex {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
```

2.Set the url for the BlogCreateView view in urls.py
```
#blog/urls.py
from django.urls import path
from .views import blogs,  blog_detail, BlogCreateView

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), 
    path('blogs/blog_create/', BlogCreateView.as_view(), name='blog_create'),
]
```
3.Create BlogCreateView in blog/views.py
```
#blog/views.py
from django.views.generic.edit import CreateView # new

class BlogCreateView(CreateView): # new
    model = Blog
    template_name = 'blogs/blog_create.html'
    fields = ['title','subtitle', 'author', 'body']

```
4.Create the blog_create.html in templates/blogs/ and add a form
```
{% extends 'base.html' %} 
{% block content %}
<h1>Create a new blog</h1>
<div>
  <form action="" method="POST">
    {% csrf_token %} 
    {{ form.as_p }}
    <input type="submit" value="Save" />
  </form>
</div>
{% endblock content %}

```
5.Most important now, where to send the user after the form is submitted, 
the user should get redirected to the blogs page after the form is submitted.
for this we have to add a get_absolute_url() method in the blog model.
get_absolute_url() method is used to redirect the user after the form is submitted.


#### Update our blog/models.py , add get_absolute_url() method to redirect the user after the form is submitted to the blogs page.
```
#blog/models.py
from django.db import models
from django.urls import reverse #new

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)  #ForeignKey allows many-to-one relationships between models , this means a author can have many blog posts
    #on_delete=models.CASCADE means if the author is deleted, all the blog posts associated with that author will be deleted as well.
    #auth.User is the name of the model that we are referencin to the user model that Django provides for authentication.
    body = models.TextField()

    def get_absolute_url(self): # add this method
        return reverse('blog_detail', args=[str(self.id)])

    
    def __str__(self):
        return self.title

```
6.  Restart the server
7.  Create a blog entry

## Let's redesign our form to make it more user friendly. In order to style django forms we need to create a forms.py file in the blog app. 
1. Create a new file forms.py in blog app
```
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:  # Meta class is used to specify additional options for a form
        model = Blog
        fields = ['title', 'subtitle', 'body', 'author']

        #now to do the styling add widgets to the form
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'})

        }
```
2. Update our views.py in blog app  
```
from .forms import BlogForm

class BlogCreateView(CreateView): # new
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/blog_create.html'
    # fields = ['title','subtitle', 'author', 'body']  #or fields = '__all__'
   

```
3. Update the form in the blog_create.html template
```
#blogs/blog_create.html
{% extends 'base.html' %} 
{% block content %}
<h1>Create a new blog</h1>
<div>
  <form action="" method="POST" class="form">
    {% csrf_token %} 
    {{ form }}
    <button type="submit" value="Save" class="btn"/>Save</button>
  </form>
</div>
{% endblock content %}
```
4. Add css for the form in base.css in the last 
```
/* form styling starts */

.form{
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 5rem;
  margin-block: 2rem;
}

.form label{
  font-family: "DM Sans", sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 1.8rem;
  color: #181717;
}


.form-control{
  border-radius: 0;
  border: none;
  border-bottom: 1px solid #181717;
  background: transparent;
  color: #181717;
  font-size: 1.8rem;
  font-family: "DM Sans", sans-serif;
  font-weight: 500;
  padding: 0.5rem;
  width: 100%;
  margin-bottom: 1.5rem;
}

.btn{
  border-radius: 0;
  border: none;
  background: #181717;
  color: #fff;
  font-size: 2rem;
  font-family: "DM Sans", sans-serif;
  font-weight: 500;
  padding: 0.5rem 1rem;
  cursor: pointer;
  /* width: 100%; */
  margin-bottom: 1.5rem;
  display: inline-block;
  max-width: 15%;
}

/* form styling ends */

```
5. Restart the server
6. Create a blog entry



### Edit/Update the blog
1. Add a edit blog link to the blog detail page
```
#templates/blogs/blog_detail.html
{% extends 'base.html' %}
{% block content %}
<a href="{% url 'blogs' %}" class="nav-links underline mb-4">Back to blogs</a>
<h1 class="hero-title">
    {{ blog.title }}
  </h1>
  <div class="blogs">
 
    <div class="blog-card">
    <div class="blog-card-text">
        <div>
          <h4 class="blog-card-title">{{ blog.subtitle }}</h4>
          <p class="blog-card-subtitle">
            posted by <em>{{ blog.author }}</em> 
          </p>
          <p class="blog-card-para">
            {{ blog.body }}
          </p>
        </div>
        <a href="{% url 'blog_edit' blog.pk %}" class="nav-links underline">Edit this blog</a>
      </div>

  </div>
 
</div>
 

{% endblock content %}

```
2. Set the url and add the BlogUpdateView view
```
#blog/urls.py
from django.urls import path
from .views import blogs,  blog_detail, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), 
    path('blogs/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'), # new
]


#blog/views.py
from django.views.generic.edit import CreateView,UpdateView

class BlogUpdateView(UpdateView): # new
    model = Blog
    #form_class = BlogForm
    template_name = 'blogs/blog_edit.html'
    fields = ['title','subtitle', 'body']  

```
3. Create a blog_edit.html template almost as same as blog_create.html
```
{% extends 'base.html' %} 
{% block content %}
<h1 class="hero-title">Edit this blog</h1>
<div>
  <form action="" method="POST" class="form">
    {% csrf_token %} 
    {{ form }}
    <button type="submit" value="Save" class="btn"/>Update</button>
  </form>
</div>
{% endblock content %}

```


4. Add css for the form in base.css in the last
```
.form input{

  border-radius: 0;
  border: none;
  border-bottom: 1px solid #181717;
  background: transparent;
  color: #181717;
  font-size: 1.8rem;
  font-family: "DM Sans", sans-serif;
  font-weight: 400;
  padding: 0.5rem;
  width: 100%;
  margin-bottom: 1.5rem;

}
```
5. Restart the server and Edit some blogs



### Delete the blog

1.  Add a link to delete the blog in the blog detail page
```
{% extends 'base.html' %}
{% block content %}
<a href="{% url 'blogs' %}" class="nav-links underline mb-4">Back to blogs</a>
<h1 class="hero-title">
    {{ blog.title }}
  </h1>
  <div class="blogs">
 
    <div class="blog-card">
    <div class="blog-card-text">
        <div>
          <h4 class="blog-card-title">{{ blog.subtitle }}</h4>
          <p class="blog-card-subtitle">
            posted by <em>{{ blog.author }}</em> 
          </p>
          <p class="blog-card-para">
            {{ blog.body }}
          </p>
        </div>
          <div class="flex">
          <a href="{% url 'blog_edit' blog.pk %}" class="nav-links underline">Edit this blog</a>
          <a href="{% url 'blog_delete' blog.pk %}" class="nav-links underline color-red">Delete this blog</a>
        </div>
      </div>

  </div>
 
</div>
 

{% endblock content %}

```
2. Set the url and add the BlogDeleteView view
```
#blog/urls.py
from django.urls import path
from .views import blogs,  blog_detail, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), 
    path('blogs/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'), 
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),#new
]

#blog/views.py
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy # new

class BlogDeleteView(DeleteView): # new
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blogs')    

```           
3. Add blog_delete.html template 
```
#blogs/blog_delete.html
{% extends 'base.html' %} 
{% block content %}
<h1 class="hero-title">Delete this Blog</h1>
<div>
  <form action="" method="POST" class="form">
    {% csrf_token %}
    <p class="blog-card-subtitle">Are you sure you want to delete "{{ blog.title }}"?</p>
    <br />
    <button type="submit" value="Confirm" class="btn" />Confirm</button>
  </form>
</div>
{% endblock content %}

```
4. Delete some blogs


## Add a header image to the blog
1. Update our Blog model
```
#blog/models.py
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)  #ForeignKey allows many-to-one relationships between models , this means a author can have many blog posts
    body = models.TextField()
    # description = models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    subtitle = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('blog_detail', args=[str(self.id)])
```
2. Install Pillow, use this commands in the terminal
```
pip install Pillow
```
3. Makemigrations and migrate our model
```
python manage.py makemigrations blog
python manage.py migrate
```
4. Update the requirements.txt  
```
pip freeze >requirements.txt
```
5. Update the BlogForm in blog/forms.py
```
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:  # Meta class is used to specify additional options for a form
        model = Blog
        fields = ['title', 'subtitle', 'body', 'author','header_image']  #new

        #now to do the styling add widgets to the form
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control'}) #new
        }
```

6. Update the settings.py file 
```
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

```
7. Update the project urls.py file
```

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('posts.urls')),
    path('', include('blog.urls')), # new
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
8. Update the blogs.html and blog_detail.html template to display the image
```
#blogs/blogs.html ,add this before blog-card-text
  <div class="blog-card-img">
        <img src="{{blog.header_image.url}}" alt="" class="img-responsive">
      </div>

#blogs/blog_detail.html, add this before blog-card-text
  <div class="blog-card-img">
        <img src="{{blog.header_image.url}}" alt="" class="img-responsive">
      </div>  
# add this to base.css
.img-responsive {
  max-width: 100%;
  height: auto;
}
       
```

9. Update the blog_edit.html and BlogEditView
```
#blogs/blog_edit.html
{% extends 'base.html' %} 
{% block content %}
<h1 class="hero-title">Edit this blog</h1>
<div>
  <form action="" method="POST" class="form" enctype="multipart/form-data">
    {% csrf_token %} 
    {{ form }}
    <button type="submit" value="Save" class="btn"/>Update</button>
  </form>
</div>
{% endblock content %}


#blog/views.py
class BlogUpdateView(UpdateView): # new
    model = Blog
    # form_class = BlogForm
    template_name = 'blogs/blog_edit.html'
    fields = ['title','subtitle', 'body','header_image']  

```
10. Update the blog_create.html
```

{% extends 'base.html' %} 
{% block content %}
<h1 class="hero-title">Create a new blog</h1>
<div>
  <form action="" method="POST" class="form" enctype="multipart/form-data">
    {% csrf_token %} 
    {{ form }}
    <button type="submit" value="Save" class="btn"/>Save</button>
  </form>
</div>
{% endblock content %}
```



11. Run the server