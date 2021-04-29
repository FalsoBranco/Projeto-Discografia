from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from disco.models import Musica


# Create your views here.
def index(request: HttpRequest):
    context = {}
    return render(request, "disco/index.html", context)


class MusicaListView(ListView):
    model = Musica
    template_name = "disco/musica_lista.html"
    context_object_name = "musicas"
