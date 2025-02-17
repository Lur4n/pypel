from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q, F, Count, Subquery, OuterRef, FloatField, Sum, ExpressionWrapper
from .models import Usuario, Perfil, Departamento
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

#CADASTRO DE DEPARTAMENTOS
@login_required
def departamentos(request):
    if request.session.get('perfil_atual') not in {'Administrador'}:
        messages.error(request, 'Você não é administrador')
        return redirect('core:main')
    
    if request.method == 'POST':
        messages.succes(request, 'Implementação vem depois')
        
    departamentos_lista = Departamento.objects.all().exclude(nome__iexact='Geral').order_by('nome')
    paginator = Paginator(departamentos_lista, settings.NUMBER_GRID_PAGES)
    numero_pagina = request.GET.get('page')
    page_obj = paginator.get_page(numero_pagina)

    return render(request, 'departamentos.html', {'page_obj': page_obj})

    


# Create your views here.
