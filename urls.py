from django.urls import path
from django.contrib.auth import views as auth_views # Import pour Login/Logout
from . import views

urlpatterns = [
    # Pages principales
    path('', views.accueil, name='accueil'),
    path('nouveau/', views.nouveau_reve, name='nouveau_reve'),
    path('public/', views.espace_public, name='espace_public'),
    path('abonnement/', views.abonnement, name='abonnement'),
    
    # Authentification
    path('inscription/', views.signup, name='signup'),
    path('connexion/', auth_views.LoginView.as_view(template_name='reves/login.html'), name='login'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),
    path('mon-journal/', views.mes_reves, name='mes_reves'),

]
