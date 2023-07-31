from django.shortcuts import render, HttpResponse
from django.views import View, generic
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . import forms


# Create your views here.
class BaseView(View):
    template_name = 'login/base.html'


def base_view(request):
    template_name = 'login/base.html'
    return render(request, template_name)


def login_view(request):
    template_name = 'login/login.html'
    login_form = forms.LoginForm()
    context = {'login_form': login_form}
    return render(request, template_name, context)