# User Accounts (login,logout and signup)
Django comes with aa built-in user management system that we can user and customize as needed.
When we create a project , Django installs auth app which provides a User Object that contains
    username
    password
    email
    first_name
    last_name

we will use this user object to log in , logout and signup users in our blog app.


## Log in
Django provides a built-in login system that we can use to log in users.
Django provides us with a default view for a log in page via LoginView

1. Update project urls.py
```
#config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', include('pages.urls')),
    path('', include('posts.urls')),
    path('', include('blog.urls')), # new
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
2.By default, the LoginView looks for registration/login.html. for login form,Lets create a new template registration/login.html
```
#templates/registration/login.html
{% extends 'base.html' %}
{% block content %}
<h2 class="hero-title">Log In</h2>
<form method="post" class="form">
{% csrf_token %}
{{ form.as_p }}
<button type="submit" class="btn">Log In</button>
</form>
{% endblock content %}

```
3.Specify where to redirect the user after successfull logging in. Update the settings.py
```
#config/settings.py
# add this at the bottom
LOGIN_REDIRECT_URL = 'home'

```
4. Run the server, go to localhost:8000/accounts/login/ and login


## Update Homepage to display message to user whether they are logged in or not
Django's is_authenticated method returns True if the user is logged in, False otherwise.
1.Add this below header in base.html
```
#templates/base.html
 <div class="container">
      {% if user.is_authenticated %}
      <h2 class="hero-title">Hi {{ user.username }}!</h2>
      {% else %}
      <p>You are not logged in.</p>
      <a href="{% url 'login' %}" class="nav-links underline">Log In</a>
      {% endif %}

    </div>
```
## Log out
1. Add logout link in the base.html
```
   <div class="container">
      {% if user.is_authenticated %}
      <div class="flex">
        <h2 class="hero-title">Hi {{ user.username }}!</h2>
        <p><a href="{% url 'logout' %}" class="nav-links color-red">Log out</a></p>
      </div>
      
      {% else %}
      <p>You are not logged in.</p>
      <a href="{% url 'login' %}" class="nav-links underline">Log In</a>
      {% endif %}

    </div>
```
2.Add a redirect link after the user logs out
```
#config/settings.py

LOGOUT_REDIRECT_URL = 'home' # new
``` 
3.Try logging out and see if you are redirected to the homepage
4.Create some more users and try login and logout again

## Sign up
Sign up page to register new users
1. Create new app called accounts fr our signup page
```
python manage.py startapp accounts

```
2.Add accounts app to settings.py INSTALLED_APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'posts',
    'blog',
    'accounts' #new
]
```
3.Set the config/urls to include the accounts app
```
#config/urls.py


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), # new
    path('', include('pages.urls')),
    path('', include('posts.urls')),
    path('', include('blog.urls')), # new
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
The order of our urls matters here because Django reads this file top-to-bottom. Therefore
when we request the /accounts/signup url, Django will first look in auth, not find it, and then
proceed to the accounts app.

4. Create accpunts/urls.py
```
#accounts/urls.py
from django.urls import path
from .views import SignUpView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

```
5. Django Provides UserCreationForm to create new users.
We can use this form to create new users.
<br>
Update the accounts/views.py
```
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

```
We’re subclassing the generic class-based view CreateView in our SignUpView class. We specify
the use of the built-in UserCreationForm and the not-yet-created template at signup.html. And
we use reverse_lazy to redirect the user to the log in page upon successful registration.
Why use reverse_lazy here instead of reverse? The reason is that for all generic class-based
views the URLs are not loaded when the file is imported, so we have to use the lazy form of
reverse to load them later when they’re available.

6.Create a new template registration/signup.html
```
#templates/registration/signup.html
{% extends 'base.html' %}
 {% block content %}
<h2 class="hero-title">Sign Up</h2>
<form method="post" class="form">
  {% csrf_token %}
   {{ form.as_p }}
  <button type="submit" class="btn">Sign Up</button>
</form>
{% endblock content %}

```
7. Run the server and go to localhost:8000/accounts/signup/ and sign up
8. Our ultimate flow : Signup -> Login -> Homepage.
9. Add a link to signup in base.html
```
#base.html
   <div class="container">
      {% if user.is_authenticated %}
      <div class="flex">
        <h2 class="hero-title">Hi {{ user.username }}!</h2>
        <p><a href="{% url 'logout' %}" class="nav-links color-red">Log out</a></p>
      </div>
      
      {% else %}
      <p class="blog-card-subtitle">You are not logged in.</p>
      <div class="flex mb-4">
        <a href="{% url 'login' %}" class="nav-links underline">Log In</a>
        {% endif %}
        <a href="{% url 'signup' %}" class="nav-links underline">Sign up</a>
      </div>
    </div>
```


10. Changes in base.html to show homepage and other pages to logged in users only

```
#templates/base.html
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
              <a href="{% url 'about' %}" class="nav-links">About</a>
              {% comment %} <a href="{% url 'contact' %}" class="nav-links">Contact</a> {% endcomment %}
              <a href="{% url 'blogs' %}" class="nav-links">Blogs</a>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <div class="container">
      {% if user.is_authenticated %}
      <div class="flex">
        <h2 class="hero-title">Hi {{ user.username }}!</h2>
        <p><a href="{% url 'logout' %}" class="nav-links color-red">Log out</a></p>
      </div>
      <main>
        <div class="container">
          {% block content %}
          {% endblock content %}
        </div>
      </main>
      {% else %}
      <p class="blog-card-subtitle">You are not logged in.</p>
      <div class="flex">
        <a href="{% url 'login' %}" class="nav-links underline">Log In</a>
        {% endif %}
        <a href="{% url 'signup' %}" class="nav-links underline">Sign up</a>
      </div>
    </div>
    <div class="container">
      {% block login %}
      {% endblock login %}
    </div>
    <div class="container">
      {% block signup %}
      {% endblock signup %}
    </div>
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
```

```
#templates/registration/login.html
{% extends 'base.html' %}
{% block login %}
<h2 class="hero-title">Log In</h2>
<form method="post" class="form">
{% csrf_token %}
{{ form.as_p }}
<button type="submit" class="btn">Log In</button>
</form>
{% endblock login %}


```
```
#templates/registration/signup.html
{% extends 'base.html' %}
{% block signup %}
<h2 class="hero-title">Sign Up</h2>
<form method="post" class="form">
  {% csrf_token %}
   {{ form.as_p }}
  <button type="submit" class="btn">Sign Up</button>
</form>
{% endblock signup %}

```
11. Restart the server