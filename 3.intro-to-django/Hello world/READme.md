Hello World App
We will build a Django project that simply says " Hello, World" on the homepage
Initial Setup-:

1.Create a virtual environment
python -m venv venv
source venv/bin/activate  
#windows users  before activating make sure to run this command in the powershell
#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

venv\Scripts\activate
2.Installing Django
pip install django~=3.2.8
#save requirements.txt
pip freeze > requirements.txt

#install requirements.txt
pip install -r requirements.txt
3......Create a Django Project
django-admin startproject config .  #notice the dot at the end of the project name
Django Project Structure
├── config
    │
    ├── __init__.py
    |
    ├── asgi.py -> helps to run Asynchronous Server Gateway Interface Apps
    │
    ├── settings.py -> controls our project's settings
    │
    ├── urls.py -> tells Django which pages to build in respsonse to a browser or URL request
    │
    └── wsgi.py -> Web Server Gateway Interface, helps Django server our eventual web pages.
│   
└── manage.py  -> used to execute various Django commands such as running the local web server or creating a new app.
4...Start the Development server
python manage.py runserver
Remove the warnings
#First stop the development server by CTRL + C
python manage.py migrate
python manage.py runserver
5........Create an App
Django uses the concept of projects and apps to keep code clean and readable. A single Django project contains one or more apps within it that all work together to power a web application.
6.....Create our first App
 python manage.py startapp pages
Django App Structure
(helloworld) $ tree
├── pages
    │
    ├── __init__.py
    │
    ├── admin.py -> configuration file for the built-in Django Admin app
    │
    ├── apps.py -> configuration file for the app itself
    │   
    ├── migrations ->migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync
        │
        └── __init__.py
    │
    ├── models.py -> where we define our database models which Django automatically translates into database tables
    │
    ├── tests.py -> for our app-specific tests
    │
    └── views.py -> where we handle the request/response logic for our web app

7...Add our new pages app to Django project
# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages', # add app here
]
URLs, Views, Models, Templates
HTTP request/response cycle.
When you type in a URL (HTTP request), such as https://www.example.com, the first thing that happens within our Django project is a URLpattern is found that matches the homepage.
The URLpattern specifies a view which then determines the content for the page (usually from a database model) and then ultimately a template for styling and basic logic. The end result is sent back to the user as an HTTP response.

#Django request/response cycle
URL -> View -> Model (typically) -> Template
views -> determine what content is displayed on a given page
urls -> determines where that content is going
model -> cotains the content from the database
template -> provides styling for the data
8....Update the view.py
# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')

9...Create and configure urls in our app (pages app)
#create a new file urls.py in our app
#configure that urls.py
#pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
        path('', homePageView, name='home'),
]

10....Update our Project urls.py
# config/urls.py
from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
]

Restart our Django Server
python manage.py runserver