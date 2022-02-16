# Custom User Model
Django recommends that you always use a custom user model, so that you can add additional fields to the user model without having to modify the code.

1. Start by updating the settings.py file to include the custom user model.
```
#config/settings.py
AUTH_USER_MODEL = 'accounts.CustomUser' # <-- Add this line our custom user model name is CustomUser
```
2.Add a new model to the accounts app call it CustomUser.
```
# accounts/models.py
from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
```

3. Create a Customuser form in the accounts app.
```
# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


```
For both new forms we are using the Meta class126 to override the default fields by setting the
model to our CustomUser and using the default fields via Meta.fields which includes all default
fields. To add our custom age field we simply tack it on at the end and it will display automatically
on our future sign up page.

4. Update admin.py to include the CustomUser model.
```
#accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

```
5. Update our blog model
```
#blog/models.py
from django.db import models
from django.urls import reverse #new
from config import settings
User = settings.AUTH_USER_MODEL
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='User')  #update the author
    body = models.TextField()
    # description = models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    subtitle = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('blog_detail', args=[str(self.id)])
```
6. Drop the database and makemigrations and migrate
```
#Delete the database file

python manage.py makemigrations accounts
python manage.py migrate
python manage.py makemigrations blog
python manage.py migrate

```
7. Create a super user
8. Update the admin.py 

## Lets update our login,signup and logout views to use our custom user model.
Since built in auth app already provides views and urls for login and logout, we only need to update our signup view to use the custom user model.
1. Update the signup view to use CustomUserCreationForm
```
#accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

```
2. To explicitly set which fields we to display on the signup page, we can change the fields in the CustomUserCreationForm class.
```
#accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age',) # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',) # new

```
3. Restart the server
