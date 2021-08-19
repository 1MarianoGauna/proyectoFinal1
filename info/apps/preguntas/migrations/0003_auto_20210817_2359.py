# Generated by Django 3.0 on 2021-08-18 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_auto_20210817_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='categoria',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='preguntas.Categoria'),
        ),
        migrations.DeleteModel(
            name='Categorias',
        ),
    ]