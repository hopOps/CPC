- Install Pillow to add  ImageField for our model

        python -m pip install Pillow

- Change settings.py from our project

        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        MEDIA_URL = '/media/'
   
 *MEDIA_URL is web_portal for this site*
   
- Add these lines in our main URL.py

        from . import views, settings
        from django.contrib.staticfiles.urls import static
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
        urlpatterns += staticfiles_urlpatterns()
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
- Add the imageField to our model 

        photo = models.ImageField(upload_to="gallery")
        
 - In our template file
 
        <img src="{{ picture.photo }}"/>