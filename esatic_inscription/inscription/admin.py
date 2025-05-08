from django.contrib import admin
from .models import Candidat

@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'sexe', 'niveau_etude', 'created_at')
    search_fields = ('nom', 'prenom', 'contact')
    list_filter = ('sexe', 'niveau_etude', 'created_at')

