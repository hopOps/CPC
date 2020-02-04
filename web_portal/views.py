from django.shortcuts import render, get_object_or_404

from .models import Picture

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the pix index.")


def index(request):
    latest_picture_list = Picture.objects.order_by('-pub_date')[:5]
    context = {'latest_picture_list': latest_picture_list}
    return render(request, 'web_portal/index.html', context)


def login(request):
    return render(request, 'login.html')


def detail(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    return render(request, 'web_portal/detail.html', {'picture': picture})


