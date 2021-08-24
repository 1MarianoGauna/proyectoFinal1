from django import forms
from django.forms import BaseInlineFormSet

from .models import Pregunta, ElegirRespuesta, PreguntasRespondida

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, get_user_model

from apps.usuarios.models import Usuario

User = Usuario

class ElegirInlineFormset (forms.BaseInlineFormSet):
	def clean(self):
		super(ElegirInlineFormset, self).clean()


		respuesta_correcta = 0

		for formulario in self.forms:
			if not formulario.is_valid():
				return


			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta +=1


		try:

			assert respuesta_correcta == Pregunta.n_respuestas_permitidas


		except AssertionError:
			raise forms.ValidationError('Una sola respuesta es permitida')



class FormularioRegistro(UserCreationForm):

	class Meta:
		model = User

		fields = [

		'username',
		'password1',
		'password2',



		]

