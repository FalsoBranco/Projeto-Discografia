from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from disco.models import Album, Banda, Musica


# Create your views here.
def index(request: HttpRequest):
    context = {}
    return render(request, "disco/index.html", context)


class MusicaListView(ListView):
    model = Musica
    template_name = "disco/musica_lista.html"
    context_object_name = "musicas"


class BandaDetailView(DetailView):
    model = Banda
    template_name = "disco/banda_detalhe.html"
    context_object_name = "banda"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "disco/album_detalhe.html"
    context_object_name = "album"
