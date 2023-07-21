from django.urls import path, include
from . import views

app_name = 'dlar'
urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('adduser', views.add_user, name='add')
]