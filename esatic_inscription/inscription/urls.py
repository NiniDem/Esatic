from django.urls import path
from .views import inscription_view, accueil

urlpatterns = [
    path('formulaire/', inscription_view, name='inscription'),
    path('accueil/', accueil, name='accueil')
]
