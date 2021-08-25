from django.urls import path, include

from .views import jugar, resultado_pregunta

from apps.usuarios.views import registro

#app_name = 'preguntas'

urlpatterns = [
   
    path('jugar/', jugar, name = 'jugar'),

    path('resultado/<int:pregunta_contestada_pk>/', resultado_pregunta, name = 'resultado'),



]