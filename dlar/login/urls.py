# from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'login'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.base_view, name='base'),
    path('login/', views.login_view, name='login')
]
