from django.apps import AppConfig

class RevesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reves'
    
    # Adiciona um nome amigável e profissional para o painel administrativo do Django
    verbose_name = 'Gestion des Rêves 🌙'
