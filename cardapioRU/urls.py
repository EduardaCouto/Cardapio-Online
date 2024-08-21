
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls as url_django
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('accounts/', include(url_django)),
    path('accounts/', include("accounts.urls")),
    path('cardapio/', include('cardapio.urls')),
    path('pessoa/', include('pessoa.urls')),
    path('restricao/', include('restricao.urls')),
    path('alimentos/', include('alimentos.urls')),
    path('feedback/', include('feedback.urls')),
    path('equipe/', include('equipeTrabalho.urls')),
]
