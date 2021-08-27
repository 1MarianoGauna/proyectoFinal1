from django.db import models
from django.conf import settings
import random
from apps.usuarios.models import Usuario

User = settings.AUTH_USER_MODEL

# Create your models here.

class Categoria(models.Model):
	categoria = models.CharField(max_length=20)

	def __str__(self):
		return self.categoria



class Pregunta(models.Model):
	
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=True, null=False)
	texto = models.TextField(verbose_name='Texto de la pregunta')
	max_puntaje = models.DecimalField(verbose_name='Puntaje Maximo', default = 1, decimal_places = 2, max_digits= 6)
	n_respuestas_permitidas = 1

	def __str__(self):
		return self.texto




class ElegirRespuesta(models.Model):
 

	pregunta = models.ForeignKey(Pregunta, related_name='opcion', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')
	MAXIMO_RESPUESTA = 3

	def __str__(self):
		return self.texto


class Jugador(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

	def nuevo_intento(self, pregunta):
		intento = PreguntasRespondida(pregunta=pregunta, jugadorP = self)
		intento.save()

	def nueva_pregunta (self):
		respondidas = PreguntasRespondida.objects.filter(jugadorP=self).values_list('pregunta__pk', flat=True)
		preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
		
		if not preguntas_restantes.exists():
			return None 

		return random.choice(preguntas_restantes)

	def probar_intento(self,pregunta_contestada, respuesta_elegida):
		if pregunta_contestada.pregunta_id != respuesta_elegida.pregunta_id:
			return

		pregunta_contestada.respuesta_elegida = respuesta_elegida
		if respuesta_elegida.correcta is True:
			pregunta_contestada.correcta = True
			pregunta_contestada.puntaje_obtenido = respuesta_elegida.pregunta.max_puntaje
			pregunta_contestada.respuesta = respuesta_elegida

		else:
			pregunta_contestada.respuesta = respuesta_elegida

		pregunta_contestada.save()
		self.puntaje_actualizado()

	def puntaje_actualizado(self):
		ultimo_puntaje = self.intentos.filter(correcta = True).aggregate(models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

		self.puntaje_total = ultimo_puntaje
		self.save()

class PreguntasRespondida(models.Model):
	
	jugadorP = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null = True)
	correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)