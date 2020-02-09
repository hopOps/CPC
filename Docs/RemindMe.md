# Django RemindMe


## Install Django

Install Django

    pip install django

## Django Startup

Create django project

    django-admin.py startproject CPC .

Create app in django

    python manage.py startapp web_portal
    
    # For users management
    python manage.py startapp users

Don't forget to register the application in *settings.py* file:
    
    INSTALLED_APPS [
    'web_portal',
    ]
    
    INSTALLED_APPS [
    'users',
    ]

## Django Models

Modifying Models

    python manage.py makemigrations web_portal
    python manage.py sqlmigrate web_portal 0001
    python manage.py migrate
    

## Django Admin

Create a admin

    python manage.py createsuperuser

Run a Server

    python manage.py runserver
   

Playing with the API

    python manage.py shell


    >>> from web_portal.models import Picture, Category, Author  # Import the model classes we just wrote.

    # No questions are in the system yet.
    >>> Picture.objects.all()
    <QuerySet []>

Register a model in Admin Console
Edit *portal_web/admin.py* and add this line : 

    admin.site.register(Author)
    

## Django Dev

Add this line in he list urlpatterns (file .\urls.py):

    path('portal_web/', include('portal_web.urls')),
	
templateView:

<https://docs.djangoproject.com/en/3.0/intro/tutorial04/>

	- view.py
	
	from django.views import generic
	
	class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
	
	- urls.py
	
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	
*note: It's pk that is return with the DetailView generic*
	
	