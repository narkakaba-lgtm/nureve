from django.db import models
from django.contrib.auth.models import User

class Reve(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reves')
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    
    # Adicionado db_index para que a filtragem por data seja ultra rápida no diário
    date_creation = models.DateTimeField(auto_now_add=True, db_index=True)
    
    # Adicionado db_index porque o feed público filtrará constantemente por este campo
    est_public = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-date_creation'] # Sonhos mais recentes primeiro no diário e feed

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    reve = models.ForeignKey(Reve, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    texte = models.TextField()
    
    # Adicionado db_index para ordenar as discussões rapidamente
    date_publication = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        # CORREÇÃO: Removido o '-' para as mensagens seguirem a ordem cronológica correta de um chat (antigas acima, novas abaixo)
        ordering = ['date_publication'] 

    def __str__(self):
        return f"Réponse de {self.auteur.username} sur {self.reve.titre}"
