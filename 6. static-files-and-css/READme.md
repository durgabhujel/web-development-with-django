Static files and CSS
Initial Setup
python manage.py startapp blog

#Add pages to config/settings.py
#config/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'pages',
        'posts',
        'blog' #new
    ]


Database Models for our blog app
Add the following code to the blog/models.py file:
# blog/models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)  #ForeignKey allows many-to-one relationships between models , this means a author can have many blog posts
    body = models.TextField()

    def__str__(self):
        return self.title
Register the Blog model with the admin site
#blog/admin.py
from django.contrib import admin
from .models import Blog  #new

admin.site.register(Blog)  #new
Activate the Model
python manage.py makemigrations blog
python manage.py migrate
Run the server
python manage.py runserver
Django Admin
Lets go to django admin and create two blog post. To acess django admin you must have a superuser account.

To use django admin , first create a super user
python manage.py createsuperuser

Username (leave blank to use 'bickkysahani'): bickky
Email address: 
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

Start the development server
python manage.py runserver
Open the admin page, on web browser go to http://127.0.0.1:8000/admin/
Add two blog posts
Views/Templates/URLs
In order to display the posts (database content), we need to create a view

Add a Blog view to the blog/views.py file
# blog/views.py
from django.shortcuts import render

from .models import Blog

#function based view
def blogs(request):
    context = {
        'blogs': Blog.objects.all()  # Blog.objects.all() is a QuerySet object (list of objects) from the Blog model (Blog.objects.all() is a list of Blog objects)
    }
    return render(request, 'blogs/blogs.html', context)
Create a new template for the blogs page
#templates/blogs/blogs.html
<h1>Blogs Page</h1>
    <div>
        {% for blog in blogs %}
        <h1>{{ blog.title }}</h1>
        <h2>{{ blog.author }}</h2>
         <p>{{ blog.body }}</p>
        <br>
        {% endfor %}
    </div>

Create urls.py file in the blog/urls.py file
#blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogs , name='blogs'),
]
Include blog/urls.py in the main urls.py file in the root directory
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), 
    path('posts/', include('posts.urls')), 
    path('blogs/', include('blog.urls')), # new

]

Run the server
python manage.py runserver
Go to this url http://127.0.0.1:8000/blogs/
Add link to the blogs page in our home page (base.html)
Add link to blogs page in the base.html file
#templates/base.html
  <header>
        <nav>
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'about' %}">About</a>
            <a href="{% url 'contact' %}">Contact</a>
            <a href="{% url 'posts' %}">Posts</a>
            <a href="{% url 'blogs' %}">Blogs</a>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock content %}
    </main>
Extend the blogs.html file to base.html
#templates/blogs/blogs.html
{% extends 'base.html' %}
{% block content %}
    <h1>Blogs Page</h1>
    <div>
        {% for blog in blogs %}
        <h1>{{ blog.title }}</h1>
        <h2>{{ blog.author }}</h2>
        <p>{{ blog.body }}</p>
        <br />
    {% endfor %}
    </div>
{% endblock content %}

Restart the server
python manage.py runserver
Small update -> move all home.html,contact.html,about.html to pages directory inside templates and update the views accordingly
Static files
CSS, JavaScript, and images are the static files.

Add Static files to our project
Create a static folder in root directory

Add CSS and js folder in static folder

Add base.css in the css folder

Tell Django to look for static files in the static folder, update the settings.py file

#config/settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))] # new
Add some style in base.css
#static/css/base.css
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    background-color: cadetblue;
}
Add Static files to our templates (base.html) we only have to add the static files in the base.html file since all other templates are inheriting from base.html
<!-- templates/base.html -->
{% load static %}
<html>
<head>
<title>Document</title>
<link rel="stylesheet" href="{% static 'css/base.css' %}">
</head>
...
Run the server
python manage.py runserver
Now lets update our CSS file to make templates look better
Individual Blog pages
Now let's add the functionality to display the individual blog pages. For this we will create a new view, a new url and new template.

Create a new view in the blog/views.py file
#blog/views.py
def blog_detail(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_detail.html', context)
Create a new template for the blog detail page
#templates/blogs/blog_detail.html
{% extends 'base.html' %}
{% block content %}
    <h1>Blog Detail Page</h1>
    <div>
      
        <h1>{{ blog.title }}</h1>
        <h2>{{ blog.author }}</h2>
        <p>{{ blog.body }}</p>
      
    </div>
{% endblock content %}
Create a new url in the blog/urls.py file
#blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogs , name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), #new
]

All the blog posts entries will start with /blogs/ int:id -> primary key of the blog post, django automatically adds auto-incrementing primary key to our database model. we can access this primary key by using the either id or pk

Start the server and go to this url http://localhost:8000/blogs/1/ to see the blog detail page

Now update the links on the blogs.html template so that it links to the blog detail page

#templates/blogs/blogs.html
{% extends 'base.html' %}
{% block content %}
    <h1>Blogs Page</h1>
    <div>
        {% for blog in blogs %}
        <a href="{% url 'blog_detail' blog.id %}">
        <h1>{{ blog.title }}</h1>
        <h2>{{ blog.author }}</h2>
        <p>{{ blog.body }}</p>
        </a>
        <br />
    {% endfor %}
    </div>
{% endblock content %}

Now run the server
python manage.py runserver
Now you can also style the blogs.html, blog_detail.html template to make it look better

Create a new style.css file in the static/css folder and add some style to it and link that css to the template accordingly

Push the changes to GitHub

Major Redesign of this Project
Update the base.html template
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/base.css' %}" />
  </head>
  <body>
    <header>
      <nav class="navigation-bar">
        <div class="container">
          <div class="navbar-content">
            <a href="{% url 'home' %}" class="nav-logo">Bickky.</a>
            <div class="navbar-links">
              {% comment %} <a href="{% url 'about' %}" class="nav-links">About</a>
              <a href="{% url 'contact' %}" class="nav-links">Contact</a> {% endcomment %}
              <a href="{% url 'blogs' %}" class="nav-links">Blogs</a>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <main>
      <div class="container">
        {% block content %}
        {% endblock content %}
      </div>
    </main>
    <footer>
        <div class="container">
          <div class="footer">
            <h6 class="footer-title">Bickky Sahani
            </h6>
            <div class="social-links">
              <a href="#" class="social-link">Facebook</a>
              <a href="#" class="social-link">Linkedin</a>
              <a href="#" class="social-link">Twitter</a>
            </div>
          </div>
        </div>
      </footer>
  </body>
</html>

2.Update home.html template


{% extends 'base.html' %}

{% block content %}
<div class="hero-content">
    <div class="hero-text">
      <h1 class="hero-title">
        Hi I’m Bickky , FullStack Python Developer and Programming Instructor.
      </h1>
      <p class="hero-para">I work as a freelance fullstack python developer and as a remote programming instructor</p>
      <p class="hero-para">
        As a python devleoper, I make websites and web applications using python, django, html,css, javascript, bootstrap, and react.
        As a programming instructor, I teach python, django, html,css, javascript, bootstrap, and react to students all over the Nepal.
      </p>
    </div> 
    <div class="hero-img">
        {% load static %}
        <img src="{% static 'img/hero-img.png' %}" alt="" class="img-responsive">
    </div>

  </div>
  <div class="skills">
    <h5>Skills</h5>
    <div>
      <p>Python, Django, HTML,CSS, Javascript, React</p>
      <p>Postgres, MongoDB, Nodejs,Git, Github</p>
    </div>
  </div>
  <div class="softwares">
    <h5>Tools</h5>
    <div>
      <p>Visual Studio Code, Postman, Docker</p>
      </p>
     
    </div>
  </div>

  <hr class="line">
  <div class="contact">
    <h2>Get in touch with me &rarr; </h2>
    <div class="contact-links">
      <a href="mailto:makifkarasu@gmail.com">bickkysahani@gmail.com</a>
      <a href="#" target="_blank">View Resume</a>
  </div>
</div>
{% endblock content %}

Update blogs.html template
{% extends 'base.html' %}
{% block content %}
<h1 class="hero-title">
    My recent blogs
  </h1>
  <div class="blogs">
    {% for blog in blogs %}
    <div class="blog-card">
    <div class="blog-card-text">
        <div>
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

4.Update blogs_detail.html template

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
          <h4 class="blog-card-title">{{ blog.title }}</h4>
          <p class="blog-card-subtitle">
            posted by <em>{{ blog.author }}</em> 
          </p>
          <p class="blog-card-para">
            {{ blog.body }}
          </p>
        </div>
        
      </div>

  </div>
 
</div>
 

{% endblock content %}
Update base.css
@import url("https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap");

@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html {
  font-size: 62.5%;
  scroll-behavior: smooth;
}
body {
  background-color: #f3f3f3;
}

.container {
  max-width: 120rem;
  margin: 0 auto;
}

.img-responsive{
    max-width: 100%;
    height: auto;
}

/* header starts */
.navigation-bar {
  margin-top: 5rem;
  margin-bottom: 10rem;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
}

.navbar-links {
  display: flex;
  gap: 5rem;
}

.nav-links,
.nav-logo {
  font-family: "DM Sans", sans-serif;
  font-size: 2.4rem;
  font-weight: 500;
  text-decoration: none;
  color: #181717;
}
.nav-logo {
  font-size: 3.4rem;
}

/* header ends */

/* hero starts */

.hero-content {
  display: flex;
  gap: 10rem;
  margin-bottom: 10rem;
}

.hero-text{
    max-width: 75rem;
}

.hero-title {
  font-family: "DM Sans", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 6rem;
  color: #181717;
  line-height: 1.2;
  margin-bottom: 5rem;
}
.hero-para {
  font-family: "DM Sans", sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 3.2rem;
  color: #606060;
  line-height: 1.24;
  margin-bottom: 3rem;
}

/* hero ends */

/*software and skills starts */

.skills,.softwares {
  display: flex;
  gap: 3rem;
}
.softwares {
  margin-bottom: 5rem;
}
.skills {
  margin-bottom: 5rem;
}

.softwares h5,
.skills h5 {
  font-family: "Inter", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 1.8rem;
  color: #181717;

  text-decoration: underline;
  flex-basis: 16%;
}

.softwares p,
.skills p {
  font-family: "Inter", sans-serif;
  font-weight: normal;
  font-size: 1.8rem;
  color: #181717;
}

.softwares p:nth-child(1) {
  margin-bottom: 2.4rem;
}
.skills p {
  margin-bottom: 2.4rem;
}
.line {
  height: 2px;
}

/*software and skills ends */


/* contact starts */
.contact {
    display: flex;
    justify-content: space-between;
    margin-top: 7.8rem;
    margin-bottom: 19rem;
  }
.contact h2 {
    font-family: "DM Sans", sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 3.2rem;
    color: #181717;
    max-width: 19ch;
  }
  
  .contact-links a:nth-child(1) {
    font-family: "DM Sans", sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 3.2rem;
    color: #181717;
    text-decoration: none;
    display: block;
    margin-bottom: 2.8rem;
  }
  .contact-links a:nth-child(2) {
    font-family: "Inter", sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: 1.8rem;
    color: #181717;
    text-decoration: none;
  }

/* contact ends */


/* footer starts */
.footer {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5rem;
  }
  
  .footer h6 {
    font-family: "DM Sans", sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 2.2rem;
    color: #2429af;
  }
  
  .social-links {
    display: flex;
    gap: 3rem;
  }
  .social-link {
    font-family: "DM Sans", sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 2.1rem;
    color: #181717;
    text-decoration: none;
  }
  
/* footer ends */

/* blog page css starts */

.blog-card {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: 5rem;
  }
  
  .blog-card-title,
  .blog-card-subtitle,
  .blog-card-para,
  .blog-card-link {
    font-family: "Inter", sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 1.8rem;
    color: #181717;
  }
  
  .blog-card-title {
    font-size: 4.2rem;
    text-transform: uppercase;
    font-weight: 500;
    margin-bottom: 2.5rem;
  }
  
  .blog-card-subtitle {
    margin-bottom: 3.5rem;
  }
  
  .blog-card-para {
    font-size: 3rem;
    line-height: 1.4;
    color: #606060;
    margin-bottom: 2rem;
  }
  
  .blog-card-text {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .blog-card-link{
    font-weight: 500;
    texxt-decoration: underline;
    margin-bottom: 3rem;
  }
  
  .card{
    margin-top: 114px;
    margin-bottom: 114px;
  }
  
  .color-grey{
    color: #606060;
  }

  .underline{
    text-decoration: underline;
  }

  .mb-4{
    margin-bottom: 4rem;
    display: inline-block;
  }

  /* blog page css emds */
Update img folder , add one image to home.html
HTML, CSS changes ends, Now back to the BACKEND
Update our Blog Model
#blog/models.py
from django.db import models
from django.urls import reverse #new

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)  #ForeignKey allows many-to-one relationships between models , this means a author can have many blog posts
    body = models.TextField()
    # description = models.TextField()
    subtitle = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title
2.Migrate the updated model to reflect changes

python manage.py makemigrations blog
python manage.py migrate
Add new blogs from the admin page