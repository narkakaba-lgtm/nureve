from django.db import models
from django.contrib.auth.models import User

class Reve(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    est_public = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

# --- NOUVEAU : Modèle pour les réponses (Duane, Tuuwart, etc.) ---
class Commentaire(models.Model):
    # Relie le commentaire à un rêve spécifique
    reve = models.ForeignKey(Reve, on_delete=models.CASCADE, related_name='commentaires')
    # Relie le commentaire à celui qui répond
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    texte = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_publication'] # Les nouveaux messages en premier

    def __str__(self):
        return f"Réponse de {self.auteur.username} sur {self.reve.titre}"
