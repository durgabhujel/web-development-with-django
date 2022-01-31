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