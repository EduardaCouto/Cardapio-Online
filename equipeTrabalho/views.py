from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipe
from .forms import EquipeForm


def create_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_equipe')
    else:
        form = EquipeForm()
    return render(request, 'equipe/equipe_form.html', {'form': form})


from django.shortcuts import render
from .models import Equipe

def list_equipe(request):
    equipes = Equipe.objects.all()
    is_nutricionista = request.user.groups.filter(name='nutricionista').exists()

    contexto = {
        'equipes': equipes,
        'isNutri': is_nutricionista,
    }

    return render(request, 'equipe/equipe.html', contexto)



def update_equipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('list_equipe')
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'equipe/equipe_edit.html', {'form': form})


def delete_equipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        equipe.delete()
        return redirect('list_equipe')
    return render(request, 'equipe/equipe_confirm_delete.html', {'equipe': equipe})
