from django.shortcuts import render, redirect, get_object_or_404

from .models import Jugador, Pregunta, PreguntasRespondida

# Create your views here.

def jugar(request):

	jugadorp, created = Jugador.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_contestada = jugadorp.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_elegida = pregunta_contestada.pregunta.opcion.get(pk=respuesta_pk)

		except ObjetoNoExiste:
			raise Http404

		jugadorp.probar_intento(pregunta_contestada, opcion_elegida)

		return redirect('resultado', pregunta_contestada.pk)




	else:
		pregunta = jugadorp.nueva_pregunta()

		if pregunta is not None:
			jugadorp.nuevo_intento(pregunta)

		context = {
		     'pregunta':pregunta
		}

	return render(request, 'play/jugar.html', context)


def resultado_pregunta(request, pregunta_contestada_pk):
	respondida = get_object_or_404(PreguntasRespondida, pk=pregunta_contestada_pk)

	context = {

		'respondida' : respondida

	}

	return render(request, 'play/resultados.html', context)