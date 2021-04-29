from django.urls import path

from . import views

app_name = "discos"

urlpatterns = [
    path("", views.index, name="index"),
    path("discos/", views.MusicaListView.as_view(), name="discos"),
]
