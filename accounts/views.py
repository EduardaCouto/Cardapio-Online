from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UsuarioForm

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'registration/register.html', {'form': form})