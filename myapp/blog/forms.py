<<<<<<< HEAD
from attr import field
=======
>>>>>>> ddddba61ff043d981211675a4a7c8299d4509b2d
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['id','title','content','image']