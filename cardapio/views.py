from django.shortcuts import render, redirect, reverse
from .models import Cardapio
from .forms import CardapioForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def is_nutricionista(user):
    return user.groups.filter(name="nutricionista").exists()

def is_usuario(user):
    return user.groups.filter(name="usuario").exists()

def index(request):
    return render(request, 'index.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Cardapio

@login_required
def cardapio_list(request):
    cardapios = Cardapio.objects.all()
    is_nutricionista = request.user.groups.filter(name='nutricionista').exists()
    is_cae = request.user.groups.filter(name='cae').exists()

    contexto = {
        'cardapios': cardapios,
        'isNutri': is_nutricionista,
        'isCae': is_cae,
    }

    if is_nutricionista:
        return render(request, 'home/home_nutricionista.html', contexto)
    else:
        return render(request, 'cardapio/cardapio_list.html', contexto)


@user_passes_test(is_nutricionista)
@login_required
def cardapio_create(request):
    if request.method == 'POST':
        form = CardapioForm(request.POST)
        if form.is_valid():
            cardapio = form.save(commit=False) 
            cardapio.nutricionista = request.user 
            cardapio.save()
            return redirect('home')
    else:
        form = CardapioForm()

    contexto = {
        'form': form,
        'isNutri': is_nutricionista(request.user)
    }

    return render(request, 'cardapio/cardapio_form.html', contexto)

@user_passes_test(is_nutricionista)
@login_required
def cardapio_update(request, pk):
    cardapio = Cardapio.objects.get(pk=pk)
    if request.method == 'POST':
        form = CardapioForm(request.POST, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardapioForm(instance=cardapio)
    return render(request, 'cardapio/cardapio_edit.html', {'form': form})

@user_passes_test(is_nutricionista)
def cardapio_delete(request, pk):
    cardapio = Cardapio.objects.get(pk=pk)
    if request.method == 'POST':
        cardapio.delete()
        return redirect('home')
    return render(request, 'cardapio/cardapio_confirm_delete.html', {'cardapio': cardapio})

@user_passes_test(is_nutricionista)
def delete_all_cardapio(request):
    if request.method == 'POST':
        Cardapio.objects.all().delete()
    return HttpResponseRedirect(reverse('cardapio_list'))