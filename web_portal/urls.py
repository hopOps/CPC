from django.urls import path

from . import views

app_name = 'web_portal'
urlpatterns = [
    # Home
    path('', views.IndexView.as_view(), name='index'),

    # Login Page
    path('login', views.login, name='login'),

    # Detail
    path('<int:pk>', views.DetailView.as_view(), name='detail'),

    # test
    path('', views.ListView.as_view(), name='test'),
]

