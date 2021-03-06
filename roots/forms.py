from django import forms
from .models import Portraits, Commentaire, UserProfile
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class PortraitsForm(forms.ModelForm):
    class Meta:
        model = Portraits
        fields = ('nom','prenom','date_naissance','date_mort','description','faits','fonctions','oeuvres',)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('texte',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)
