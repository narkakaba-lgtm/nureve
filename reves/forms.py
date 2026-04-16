from django import forms
from .models import Reve, Commentaire # N'oublie pas d'importer Commentaire

class ReveForm(forms.ModelForm):
    class Meta:
        model = Reve
        fields = ['titre', 'contenu', 'est_public']
        # Optionnel : pour rendre les champs plus beaux
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Raconte ton rêve ici...'}),
        }

# --- AJOUTE CECI ---
class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['texte']
        widgets = {
            'texte': forms.Textarea(attrs={
                'placeholder': 'Répondre à ce rêve...', 
                'rows': 2,
                'style': 'width: 100%; border-radius: 10px; padding: 10px;'
            }),
        }
