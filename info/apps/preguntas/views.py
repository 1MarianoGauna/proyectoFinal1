from django.shortcuts import render

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

		return redirect(pregunta_contestada)




	else:
		pregunta = jugadorp.nueva_pregunta()

		if pregunta is not None:
			jugadorp.intentos(pregunta)

		context = {
		     'pregunta':pregunta
		}

	return render(request, 'play/jugar.html', context)
