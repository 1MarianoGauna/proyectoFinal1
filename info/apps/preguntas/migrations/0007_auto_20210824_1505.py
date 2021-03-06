# Generated by Django 3.0 on 2021-08-24 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0006_auto_20210819_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='Puntaje Maximo'),
        ),
        migrations.AlterField(
            model_name='elegirrespuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opcion', to='preguntas.Pregunta'),
        ),
        migrations.AlterField(
            model_name='preguntasrespondida',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='preguntas.ElegirRespuesta'),
        ),
        migrations.AlterField(
            model_name='preguntasrespondida',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intento', to='preguntas.Jugador'),
        ),
    ]
