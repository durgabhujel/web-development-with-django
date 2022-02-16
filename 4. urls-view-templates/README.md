# URLS, Views and Templates


### Initial Setup
```
python -m venv venv
source venv/bin/activate
pip install django~=3.2.8
django-admin startproject config .
python manage.py startapp pages

#Add pages to config/settings.py
#config/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'pages', # new
    ]

python manage.py runserver

```

## Templates
Templates -> individual html files that can be linked together and also include basic logic

1. Create a folder called templates in Project's base directory and an HTML file called home.html

2. Update our settings.py to tell Django the location of our new templates folder
```
# config/settings.py
    TEMPLATES = [
        {
            ...
            'DIRS': [str(BASE_DIR.joinpath('templates'))], # new
            ...
        },
    ]
```
3. Add some html codes in home.html

4. Next step is configure urls and views

## Class-Based Views

5. Update views
```
# pages/views.py
from django.views.generic import TemplateView #new

class HomePageView(TemplateView):
    template_name = 'home.html'  #new

```

## URLs

6. Update the project(config) urls to point at our app (pages) urls
```
# config/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
]

```

7. Create an app-level urls.py and add the following code
```
# pages/urls.py
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

```

8. Start development server
```
python manage.py runserver
```

### About page and Contact page
9. Create new templates about.html & contact.html, new views AboutPageView &  ContactPageView, and new url routes /about & /contact.

## Extending templates
Template tags take the form of <code> {% something %} </code> where the “something” is the template tag itself. <br>
To add URL links in our project we use the following
syntax: 
<code> {% url 'URL name from urls.py' %} </code>
example: 
<code> {% url 'home' %} </code>


10. Create a new html template base.html containing a header with links to our three pages

```
<!-- templates/base.html -->
<header>
    <nav>
        <a href="{% url 'home' %}">Home</a> 
        <a href="{% url 'about' %}">About</a>
        <a href="{% url 'contact' %}">Contact</a>
    </nav>
</header>
<main>
{% block content %}
{% endblock content %}
</main>
````

### Blocks can be overwritten by child templates via inheritance

11. Update home.html and about.html and extend to the base.html

```
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>This is Homepage</h1>
{% endblock content %}
```
``` 
<!-- templates/about.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>This is About page</h1>
{% endblock content %}
```
``` 
<!-- templates/contact.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>This is Contact page</h1>
{% endblock content %}
```
12. Start up the development server
```
python manage.py runserver
```