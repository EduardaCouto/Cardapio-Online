from django.shortcuts import render, get_object_or_404, redirect
from cardapio.models import Cardapio
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def is_nutricionista(user):
    return user.groups.filter(name="nutricionista").exists()

def is_usuario(user):
    return user.groups.filter(name="usuario").exists()

def index(request):
    return render(request, 'index.html')

@login_required
def criar_feedback(request, pk):
    cardapio = get_object_or_404(Cardapio, pk=pk)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.usuario = request.user
            feedback.idrefeicao = cardapio
            feedback.save()
            return redirect('cardapio_list') 
    else:
        form = FeedbackForm()
        
    return render(request, 'feedback/feedback_form.html', {'form': form, 'cardapio': cardapio})


@login_required
def list_feedback(request):
    usuario = request.user
    is_nutricionista = usuario.groups.filter(name='nutricionista').exists()
    
    if is_nutricionista:
        feedbacks = Feedback.objects.all()
    else:
        feedbacks = Feedback.objects.filter(usuario=usuario)
    
    contexto = {
        'feedbacks': feedbacks,
        'isNutri': is_nutricionista,
    }
    
    return render(request, 'feedback/feedback.html', contexto)

@login_required
def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('list_feedback')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'feedback/feedback_edit.html', {'form': form})

@login_required
def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        feedback .delete()
        return redirect('list_feedback')
    return render(request, 'feedback/feedback_confirm_delete.html', {'feedback': feedback})


