from django.db import models

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    niveau_etude = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    fichier_naissance = models.FileField(upload_to="documents/")
    fichier_certificat = models.FileField(upload_to="documents/")
    fichier_diplome = models.FileField(upload_to="documents/")
    lettre_motivation = models.FileField(upload_to="documents/")
    photo = models.ImageField(upload_to="photos/")
    created_at = models.DateTimeField(auto_now_add=True)
