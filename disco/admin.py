from django.contrib import admin

from .models import Album, Banda, Musica


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    pass


@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    pass
