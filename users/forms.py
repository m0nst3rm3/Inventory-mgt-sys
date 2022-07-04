from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Please enter your real name.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Please enter your family name.')
    email = forms.EmailField(max_length=245, help_text='example@gmail.com')
    address = forms.CharField(max_length=245, help_text='Please enter your permanent address. ')
    username = forms.CharField(max_length=30, help_text='Please enter your unique username')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'address', 'username')

    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'first_name',
    # }))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'last_name',
    # }))
    # usremail = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'email',
    #     'type': 'email',
    # }))
    # password = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'password',
    #     'type': 'password'
    # }))
    # address = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'address',
    # }))

