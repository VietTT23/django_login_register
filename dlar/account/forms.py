from django import forms
from .models import Account


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user_name', 'user_email', 'user_password', 'user_password',)
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'user_password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'user_password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'autocomplete': 'off', 'data-toggle': 'password'}),
        }


class SigninForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user_name', 'user_password',)
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'user_password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }
