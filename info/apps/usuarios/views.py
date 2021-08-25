from django.shortcuts import render, redirect

# Create your views here.


from apps.preguntas.forms import FormularioRegistro


def registro(request):

	titulo = 'Crear Cuenta'
	if request.method == 'POST':
		form = FormularioRegistro(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	else:
		form = FormularioRegistro()

	context = {

		'form' : form,
		'titulo': titulo
	}

	return render(request,'registro.html', context)

