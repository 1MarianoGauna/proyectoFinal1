from django.shortcuts import render

from .models import Jugador, Pregunta, PreguntasRespondida

# Create your views here.

def jugar(request):

	usuario, created = Jugador.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = usuario.intentos.select_related('pregunta').get(pregunta_pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta')

	else:
		respondidas = PreguntasRespondida.objects.filter(usuario=usuario).values_list('pregunta__pk', flat=True)
		pregunta = Pregunta.objects.exclude(pk__in=respondidas)

		context = {
		     'pregunta':pregunta
		}

	return render(request, 'play/jugar.html', context)
