from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logon', views.login, name='index'),
]

