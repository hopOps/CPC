from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Picture

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the pix index.")


class IndexView(generic.ListView):
    template_name = 'web_portal/index.html'
    context_object_name = 'latest_picture_list'

    def get_queryset(self):
        """Return the last five published pictures.
        return Picture.objects.order_by('-pub_date')[:5]"""
        return Picture.objects.order_by('-pub_date')
        #return len(Picture.objects.all())


# def index(request):
#     latest_picture_list = Picture.objects.order_by('-pub_date')[:5]
#     context = {'latest_picture_list': latest_picture_list}
#     return render(request, 'web_portal/index.html', context)


def login(request):
    return render(request, 'login.html')


class DetailView(generic.DetailView):
    model = Picture
    template_name = 'web_portal/detail.html'


# def detail(request, picture_id):
#     picture = get_object_or_404(Picture, pk=picture_id)
#     return render(request, 'web_portal/detail.html', {'picture': picture})


