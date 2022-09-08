from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), error_messages={'required': 'Please enter your name'})

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ), error_messages={'required': 'Please enter your password'})
