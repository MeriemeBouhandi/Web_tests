from django import forms
from .models import Portraits, Commentaire

class PortraitsForm(forms.ModelForm):
    class Meta:
        model = Portraits
        fields = ('nom','prenom','date_naissance','date_mort','description','faits','fonctions','oeuvres',)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('texte',)