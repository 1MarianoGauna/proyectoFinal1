from django.urls import path, include

from .views import jugar

from apps.usuarios.views import registro

#app_name = 'preguntas'

urlpatterns = [
    path('jugar/', jugar, name = 'jugar'),



]