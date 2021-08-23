from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, Categoria, PreguntasRespondida, Jugador

# Register your models here.

class ElegirRespuestaInline(admin.TabularInline):
	model = ElegirRespuesta
	can_delete =False
	max_num = ElegirRespuesta.MAXIMO_RESPUESTA
	min_num = ElegirRespuesta.MAXIMO_RESPUESTA

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (ElegirRespuestaInline, )
	list_display = ['texto',]
	search_fields = ['texto', 'preguntas__texto']

class PreguntasRespondidaAdmin(admin.ModelAdmin):
	list_display = ['pregunta', 'respuesta','correcta','puntaje_obtenido']

	class Meta:
		model = PreguntasRespondida



admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(Categoria)
admin.site.register(PreguntasRespondida)
admin.site.register(Jugador)


