from django.urls import path, include

from .views import jugar

#app_name = 'preguntas'

urlpatterns = [
    path('jugar/', jugar, name = 'jugar'),


]