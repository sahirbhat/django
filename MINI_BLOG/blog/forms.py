from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

from blog.models import Post,Contact


class Sign_reg(UserCreationForm):
    password1 = forms.CharField(label=' Set password', widget=forms.PasswordInput(attrs={'class': 'form-control  bg-dark text-white'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name ', 'email': ' Your  Email  '}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
                   'email': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'})
                   }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.TextInput(attrs={'class': 'form-control'})}

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','mobile','email','message']


