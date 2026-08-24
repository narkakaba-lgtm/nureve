from django import forms
from .models import Reve, Commentaire

class ReveForm(forms.ModelForm):
    class Meta:
        model = Reve
        fields = ['titre', 'contenu', 'est_public']
        widgets = {
            'titre': forms.TextInput(attrs={
                'placeholder': 'Donne un titre à ton rêve...'
            }),
            'contenu': forms.Textarea(attrs={
                'rows': 5, 
                'placeholder': 'Raconte ton rêve ici, chaque détail compte...'
            }),
            'est_public': forms.CheckboxInput(attrs={
                'class': 'checkbox-custom'
            })
        }
        # Traduz os rótulos automáticos do Django para francês limpo
        labels = {
            'titre': 'Titre du rêve',
            'contenu': 'Description',
            'est_public': 'Partager dans l\'Espace Public ?'
        }

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['texte']
        widgets = {
            'texte': forms.Textarea(attrs={
                'placeholder': 'Votre réponse...', 
                'rows': 2
            }),
        }
        labels = {
            'texte': '' # Remove o rótulo "Texte" automático para não poluir o chat de comentários
        }
