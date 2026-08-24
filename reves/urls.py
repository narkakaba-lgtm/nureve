from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- PAGES PRINCIPALES ---
    path('', views.accueil, name='accueil'),
    path('nouveau/', views.nouveau_reve, name='nouveau_reve'),
    path('public/', views.espace_public, name='espace_public'),
    path('abonnement/', views.abonnement, name='abonnement'),
    path('mon-journal/', views.mes_reves, name='mes_reves'),
    
    # --- AUTHENTIFICATION & SÉCURITÉ ---
    path('inscription/', views.signup, name='signup'),
    
    # Correção do caminho do template para alinhar com a configuração do DjangoTemplates
    path('connexion/', auth_views.LoginView.as_view(template_name='reves/login.html'), name='login'),
    
    # Rota de desconexão atualizada (Segura contra mudanças do Django 5+)
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),
]
