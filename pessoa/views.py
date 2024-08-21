from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cardapio.models import Cardapio

@login_required
def home(request):
    is_nutricionista = request.user.groups.filter(name='nutricionista').exists()
    is_cae = request.user.groups.filter(name='cae').exists()
    is_usuario = request.user.groups.filter(name='usuario').exists()
    cardapios = Cardapio.objects.all()

    contexto = {
        'isNutri': is_nutricionista,
        'isCae': is_cae,
        'isUsario': is_usuario,
        'cardapios': cardapios
    }

    if is_nutricionista:
        return render(request, 'home/home_nutricionista.html', contexto)
    elif is_cae:
        return render(request, 'home/home_cae.html', contexto)
    else:
        return render(request, 'home/home.html', contexto)
