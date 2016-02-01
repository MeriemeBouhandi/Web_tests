from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Portraits(models.Model):
    photo = models.ImageField(upload_to = '/images', default = 'images/image.jpeg')
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField()
    date_mort = models.DateField(null=True)
    description = models.TextField()
    faits = models.TextField()
    fonctions = models.TextField()
    oeuvres = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    ajouteePar = models.ForeignKey('auth.User')

    def publish(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.prenom + " " + self.nom

class Commentaire(models.Model):
    portraits = models.ForeignKey('roots.Portraits', related_name='commentaires', default = False)
    auteur = models.ForeignKey('auth.User')
    texte = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    approuve = models.BooleanField(default=False)

    def approve(self):
        self.approuve = True
        self.save()

    def __str__(self):
        return self.texte

class UserProfile(models.Model):
    avatar = models.ImageField(upload_to = '/images', default = 'images/image.jpeg')
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=30)
    adresse_mail = models.EmailField()
    user = models.OneToOneField(User, unique=True)

    def __str__(self):
        return "%s %s" % (self.pseudo)