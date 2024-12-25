from django.contrib import admin
from .models import Acteur, Film, Critique, Comment 


admin.site.register(Comment)


@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    search_fields = ('nom', 'prenom')
    ordering = ('nom',)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_sortie', 'casting')
    search_fields = ('titre',)
    list_filter = ('date_sortie',)
    ordering = ('date_sortie',)

    def acteurs_affiches(self, obj):
        return ", ".join([acteur.nom for acteur in obj.acteurs.all()])
    acteurs_affiches.short_description = 'Acteurs'

admin.site.register(Critique)