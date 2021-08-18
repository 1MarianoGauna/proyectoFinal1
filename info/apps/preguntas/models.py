from django.db import models

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


