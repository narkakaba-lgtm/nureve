from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Command(BaseCommand):
    help = "Envoie un rappel par email à tous les utilisateurs"

    def handle(self, *args, **kwargs):
        # On récupère tous les utilisateurs inscrits sur ton site
        utilisateurs = User.objects.all()

        for utilisateur in utilisateurs:
            # On vérifie si l'utilisateur a une adresse email
            if utilisateur.email:
                send_mail(
                    'NUREVE 🌙 : N\'oublie pas ton rêve !', # Sujet
                    f'Bonjour {utilisateur.username}, écris vite ton rêve sur NUREVE avant qu\'il ne s\'envole.', # Message
                    'contact@nupresentation.org', # Expéditeur
                    [utilisateur.email], # Destinataire
                )
        
        # Ce message s'affichera dans ton terminal pour confirmer que c'est fini
        self.stdout.write("Les rappels ont été générés dans le terminal !")

