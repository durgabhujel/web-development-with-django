# Database and Django admin
## Database 
Django Supports a number of database backends.

SQL databases examples:
PostgreSQL, MySQL, MariaDB, Oracle, or SQLite

NOSQL databases examples:
MongoDB, CouchDB, or Redis


For our local development environment, we will use SQLite. Because SQLite is a file-based database and simpler to use.

### Prerequisites
1. Download and install <a href="https://sqlitebrowser.org/dl/"> DBBrowser for SQLite </a>

### Initial Setup
```
python manage.py startapp posts

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
    ]


```
### Migrate to create an initial database
```
python manage.py makemigrations posts
python manage.py migrate
```
### Open db.sqlite3 in DBBrowser to see the database schema and data 

## Create a database Model
A database model is a class that defines the structure of the data in the database. It is a Python class that inherits from the django.db.models.Model class. It is just like tables in a relational database.

1. Add the following code to the posts/models.py file:
```
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

```
2. Register the Post model with the admin site
```
#posts/admin.py
from django.contrib import admin
from .models import Post  #new

admin.site.register(Post)  #new
```
3. Activate the Model
```
python manage.py makemigrations posts
python manage.py migrate
```
4. Run the server
```
python manage.py runserver
```

## Django Admin
Django admin is a tool that allows you to manage your database. It is a web interface that allows you to create, edit, and delete database models.

1. To use django admin , first create a super user
```
python manage.py createsuperuser

Username (leave blank to use 'bickkysahani'): bickky
Email address: 
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

```

2. Start the development server
```     
python manage.py runserver
``` 
3. Open the admin page, on web browser go to http://127.0.0.1:8000/admin/

4. Enter the username and password

5. Create a new post by clicking on the + Add Post button
6. Notice the name the posts object

7. Lets fix the name of the post object, by adding a __str__ method in our Post model
```
#posts/models.py
# posts/models.py
from django.db import models
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
```
8. Run the server again
```
python manage.py runserver
```

## Views/Templates/URLs
In order to display the posts (database content), we need to create a view

1. Add a posts view to the posts/views.py file
```
# posts/views.py
from django.shortcuts import render

from .models import Post

#function based view
def posts(request):
    context = {
        'posts': Post.objects.all()  # Post.objects.all() is a QuerySet object (list of objects) from the Post model (Post.objects.all() is a list of Post objects)
    }
    return render(request, 'posts/posts.html', context)
```

2. Create a new template for the posts page
```
#templates/posts/posts.html
<h1>Posts Page</h1>
    <div>
        {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>{{ post.text }}</p>
        <br>
        {% endfor %}
    </div>

```

3. Create urls.py file in the posts/urls.py file
```
#posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts , name='posts'),
]
```

4. Include posts/urls.py in the main urls.py file in the root directory
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
    path('posts/', include('posts.urls')), # new

]

```

5. Run the server
```
python manage.py runserver
```
6. Go to this url http://127.0.0.1:8000/posts/


### Create a new post in the admin page and see the post in the posts page


## Add link to the posts page in our home page (base.html)
1. Add link to posts page in the base.html file
```
#templates/base.html
  <header>
        <nav>
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'about' %}">About</a>
            <a href="{% url 'contact' %}">Contact</a>
            <a href="{% url 'posts' %}">Posts</a>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock content %}
    </main>
```

2. Extend the posts.html file to base.html
```
#templates/posts/posts.html
{% extends 'base.html' %}

{% block content %}
    <h1>This is PostsPage</h1>
    <div>
        {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>{{ post.text }}</p>
        <br>
        {% endfor %}
    </div>
{% endblock content %}
```

3. Restart the server
```
python manage.py runserver
```

## Add, Commit and Push to the remote 