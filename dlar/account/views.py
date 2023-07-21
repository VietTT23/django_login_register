from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm, SigninForm


# Create your views here.
def home(request):
    return render(request, 'account/home.html')


def signin(request):
    s = SigninForm()
    context = {'s': s}
    return render(request, 'account/signin.html', context)


def register(request):
    r = RegisterForm()
    context = {'r': r}
    return render(request, 'account/register.html', context)


def add_user(request):
    if request.method == 'POST':
        u = RegisterForm(request.POST)
        if u.is_valid():
            u.save()
            return HttpResponse('Dang ki thanh cong')
