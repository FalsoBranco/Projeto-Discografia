from typing import Any, Dict

from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from disco.forms import MusicaForm
from disco.models import Album, Banda, Musica


# Create your views here.
def index(request: HttpRequest):
    context = {}
    return render(request, "disco/index.html", context)


class MusicaListView(ListView):
    model = Musica
    template_name = "disco/musica_lista.html"
    context_object_name = "musicas"


class MusicaUpdateView(UpdateView):
    form_class = MusicaForm
    model = Musica
    template_name = "disco/musica_update.html"
    success_url = "/discos/"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["musica"] = self.object
        return context


class MusicaDeleteView(DeleteView):
    model = Musica
    template_name = "disco/musica_delete.html"
    success_url = "/discos/"


class BandaDetailView(DetailView):
    model = Banda
    template_name = "disco/banda_detalhe.html"
    context_object_name = "banda"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "disco/album_detalhe.html"
    context_object_name = "album"
