from django.contrib import admin
from .models import Reve

@admin.register(Reve)
class ReveAdmin(admin.ModelAdmin):
    # 1. Colunas que vão aparecer na tabela de listagem
    list_display = ('titre', 'auteur', 'date_creation', 'public')
    
    # 2. Barra lateral de filtros rápidos para o administrador
    list_filter = ('date_creation', 'auteur')
    
    # 3. Barra de pesquisa (procura pelo título do sonho ou pelo nome de utilizador do autor)
    search_fields = ('titre', 'contenu', 'auteur__username')
    
    # 4. Ordenação padrão (os sonhos mais recentes aparecem primeiro no topo)
    ordering = ('-date_creation',)
    
    # 5. Paginação (mostra 25 sonhos por página para o painel carregar rápido)
    list_per_page = 25
