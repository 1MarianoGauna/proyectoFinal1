# Generated by Django 3.0 on 2021-08-25 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0007_auto_20210824_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntasrespondida',
            name='usuario',
        ),
        migrations.AddField(
            model_name='preguntasrespondida',
            name='jugadorP',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='preguntas.Jugador'),
        ),
    ]
