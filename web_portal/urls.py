from django.urls import path

from . import views

app_name = 'web_portal'
urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # Login Page
    path('login', views.login, name='login'),

    # Detail
    path('<int:picture_id>', views.detail, name='detail'),
]

