from django.urls import path

from . import views

app_name = "discos"

urlpatterns = [
    path("", views.index, name="index"),
    path("discos/", views.MusicaListView.as_view(), name="discos"),
    path("discos/banda/<int:pk>", views.BandaDetailView.as_view(), name="banda_detail"),
    path("discos/album/<int:pk>", views.AlbumDetailView.as_view(), name="album_detail"),
]
