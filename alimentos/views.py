from django.shortcuts import render, get_object_or_404, redirect
from .models import Alimento
from .forms import AlimentosForm
from django.contrib.auth.decorators import login_required


def create_alimento(request):
    if request.method == 'POST':
        form = AlimentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_alimentos')
    else:
        form = AlimentosForm()
    return render(request, 'alimentos/alimentos_form.html', {'form': form})


@login_required
def list_alimentos(request):
    # Obtém o usuário que está fazendo a requisição
    usuario = request.user
    
    # Verifica se o usuário pertence ao grupo 'nutricionista'
    is_nutricionista = usuario.groups.filter(name='nutricionista').exists()
    
    # Busca todos os objetos do modelo Alimento
    alimentos = Alimento.objects.all()
    
    # Cria um contexto com a lista de alimentos e a informação se o usuário é nutricionista
    contexto = {
        'alimentos': alimentos,
        'isNutri': is_nutricionista,
    }
    
    # Renderiza o template 'alimentos/alimentos.html' com o contexto criado
    return render(request, 'alimentos/alimentos.html', contexto)



def update_alimento(request, pk):
    alimento = get_object_or_404(Alimento, pk=pk)
    if request.method == 'POST':
        form = AlimentosForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('list_alimentos')
    else:
        form = AlimentosForm(instance=alimento)
    return render(request, 'alimentos/alimentos_edit.html', {'form': form})


def delete_alimento(request, pk):
    # obtém um objeto do banco de dados baseado no modelo e filtro fornecidos.
    alimento = get_object_or_404(Alimento, pk=pk)
    if request.method == 'POST':
        alimento.delete()
        return redirect('list_alimentos')
    return render(request, 'alimentos/alimentos_confirm_delete.html', {'alimento': alimento})
