
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from apps.usuarios.views import registro
from apps.preguntas.views import jugar, resultado_pregunta, tablero


from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home, name = "home"),
    path('login/',auth.LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('logout/',auth.LogoutView.as_view(), name = 'logout'),
    path('registro/', registro, name = 'registro'),
    path('preguntas/',include('apps.preguntas.urls')),

    path('jugar/', jugar, name = 'jugar'),
    path('resultado/<int:pregunta_contestada_pk>/', resultado_pregunta, name = 'resultado'),
    path('tablero/', tablero, name = 'tablero'),


]
