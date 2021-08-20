from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Categoria(models.Model):
	categoria = models.CharField(max_length=20)

	def __str__(self):
		return self.categoria



class Pregunta(models.Model):
	
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=True, null=False)
	texto = models.TextField(verbose_name='Texto de la pregunta')
   

	def __str__(self):
		return self.texto


class ElegirRespuesta(models.Model):
 

	pregunta = models.ForeignKey(Pregunta, related_name='preguntas', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')
	MAXIMO_RESPUESTA = 3

	def __str__(self):
		return self.texto


class Jugador(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

	
class PreguntasRespondida(models.Model):
	usuario = models.ForeignKey(Jugador, on_delete=models.CASCADE)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name='intentos')
	correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)




