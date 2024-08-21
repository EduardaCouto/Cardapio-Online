from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Restricao
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group
from .forms import EditRestricaoForm
from accounts.models import Usuario



@login_required
def criar_solicitacao(request):
    usuario = Usuario.objects.get(id=request.user.id) 
    restricao = Restricao.objects.create()  
    usuario.restricao = restricao
    usuario.save() 

    return redirect('minhas_solicitacoes')


@login_required
def editar_restricao(request, id):
    restricao = get_object_or_404(Restricao, id=id)
    
    if request.method == 'POST':
        form = EditRestricaoForm(request.POST, instance=restricao)
        if form.is_valid():
            form.save()
            return redirect('listar_solicitacoes')
    else:
        form = EditRestricaoForm(instance=restricao)
    
    is_cae = request.user.groups.filter(name='cae').exists()
    
    contexto = {
        'form': form,
        'isCae': is_cae,
    }

    return render(request, 'solicitacao/solicitacao_update.html', contexto)
 
@login_required
def minhas_solicitacoes(request):
    usuario = Usuario.objects.get(id=request.user.id)  # Obtém a instância de Usuario correspondente
    restricoes = usuario.restricao
    return render(request, 'solicitacao/minhas_solicitacoes.html', {'restricoes': restricoes})

@login_required
def delete_restricao(request, id):
    restricao = get_object_or_404(Restricao, id=id)
    
    if request.method == 'POST':
        restricao.delete()
        
        if request.user.groups.filter(name='cae').exists():
            return redirect('listar_solicitacoes')
        else:
            return redirect('minhas_solicitacoes')

    is_cae = request.user.groups.filter(name='cae').exists()
    
    contexto = {
        'isCae': is_cae,
        'restricao': restricao
    }
    
    return render(request, 'solicitacao/solicitacao_confirm_delete.html', contexto)

@login_required
def listar_solicitacoes(request):

    is_cae = request.user.groups.filter(name='cae').exists()
    usuarios = Usuario.objects.filter(restricao__status='Solicitado')
    
    contexto = {
        'isCae': is_cae,
        'usuarios': usuarios,
    }
    return render(request, 'solicitacao/solicitacoes.html', contexto)