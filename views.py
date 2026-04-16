from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Ajouté pour sécuriser
from .models import Reve, Commentaire
from .forms import ReveForm, CommentaireForm

# 1. ACCUEIL
def accueil(request):
    return render(request, 'reves/accueil.html')

# 2. INSCRIPTION
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = UserCreationForm()
    return render(request, 'reves/signup.html', {'form': form})

# 3. NOUVEAU RÊVE
@login_required # Seuls les gens connectés peuvent écrire
def nouveau_reve(request):
    if request.method == "POST":
        form = ReveForm(request.POST)
        if form.is_valid():
            reve = form.save(commit=False)
            reve.auteur = request.user 
            reve.save()
            return redirect('accueil')
    else:
        form = ReveForm()
    return render(request, 'reves/nouveau_reve.html', {'form': form})

# 4. MON JOURNAL (Nouveau) : Voir seulement mes rêves à moi
@login_required
def mes_reves(request):
    # On filtre pour ne prendre que les rêves de l'utilisateur connecté
    reves_perso = Reve.objects.filter(auteur=request.user).order_by('-date_creation')
    return render(request, 'reves/mes_reves.html', {'reves': reves_perso})

# 5. ESPACE PUBLIC
def espace_public(request):
    reves_publics = Reve.objects.filter(est_public=True).order_by('-date_creation')
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
            
        form = CommentaireForm(request.POST)
        reve_id = request.POST.get('reve_id')
        
        if form.is_valid() and reve_id:
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.reve = get_object_or_404(Reve, id=reve_id)
            commentaire.save()
            return redirect('espace_public')
    else:
        form = CommentaireForm()

    return render(request, 'reves/espace_public.html', {
        'reves': reves_publics,
        'form': form
    })

# 6. ABONNEMENT
def abonnement(request):
    return render(request, 'reves/abonnement.html')
