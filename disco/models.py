from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Banda(models.Model):

    nome = models.CharField("Nome da Banda", max_length=155)

    class Meta:
        verbose_name = _("banda")
        verbose_name_plural = _("bandas")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("banda_list", kwargs={"pk": self.pk})


class Album(models.Model):

    titulo = models.CharField("Titulo do Album", max_length=155)
    banda = models.ForeignKey(
        "disco.Banda", verbose_name="Banda do Album", on_delete=models.CASCADE
    )

    data = models.DateField("Data do Album", auto_now=True)

    class Meta:
        verbose_name = _("album")
        verbose_name_plural = _("albums")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("album_musicas", kwargs={"pk": self.pk})


class Musica(models.Model):

    titulo = models.CharField("Titulo da musica", max_length=155)
    segundos = models.IntegerField("Duração da Musica")
    album = models.ForeignKey(
        "disco.Album", verbose_name="Album da Musica", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("musica")
        verbose_name_plural = _("musicas")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("musica_detail", kwargs={"pk": self.pk})

    def get_formated_music_time(self):
        return str(timedelta(seconds=self.segundos))
