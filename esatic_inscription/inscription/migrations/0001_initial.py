# Generated by Django 5.2.1 on 2025-05-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=10)),
                ('niveau_etude', models.CharField(max_length=100)),
                ('etablissement', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=20)),
                ('fichier_naissance', models.FileField(upload_to='documents/')),
                ('fichier_certificat', models.FileField(upload_to='documents/')),
                ('fichier_diplome', models.FileField(upload_to='documents/')),
                ('lettre_motivation', models.FileField(upload_to='documents/')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
