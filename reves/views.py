from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Reve, Commentaire
# CORREÇÃO: Nome do formulário corrigido no import
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
@login_required
def nouveau_reve(request):
    if request.method == "POST":
        form = ReveForm(request.POST)
        if form.is_valid():
            reve = form.save(commit=False)
            reve.auteur = request.user 
            reve.save()
            # MELHORIA: Redireciona diretamente para o diário do utilizador
            return redirect('mes_reves') 
    else:
        form = ReveForm()
    return render(request, 'reves/nouveau_reve.html', {'form': form})

# 4. MON JOURNAL
@login_required
def mes_reves(request):
    # Como adicionámos a ordenação na classe Meta do Model, o order_by() aqui já não é obrigatório
    reves_perso = Reve.objects.filter(auteur=request.user)
    return render(request, 'reves/mes_reves.html', {'reves': reves_perso})

# 5. ESPACE PUBLIC
def espace_public(request):
    reves_publics = Reve.objects.filter(est_public=True)
    
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
        # Garante que o formulário é instanciado corretamente no método GET
        form = CommentaireForm()

    return render(request, 'reves/espace_public.html', {
        'reves': reves_publics,
        'form': form
    })

# 6. ABONNEMENT
def abonnement(request):
    return render(request, 'reves/abonnement.html')
