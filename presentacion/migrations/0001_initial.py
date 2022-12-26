# Generated by Django 3.2 on 2022-07-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AireLibre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='aire_libre/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Introducción Aire Libre',
                'verbose_name_plural': 'Introducción Aire Libre',
            },
        ),
        migrations.CreateModel(
            name='CarrouselIntroduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1)),
                ('titulo', models.CharField(choices=[('---', '---'), ('Novedades', 'Novedades'), ('Ofertas', 'Ofertas'), ('Volvío a Entrar', 'Volvío a Entrar'), ('Destacados', 'Destacados')], default='---', max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='carrouselle_intro/%Y/%m/%d')),
                ('descripcion', models.CharField(blank=True, max_length=220, null=True, verbose_name='Descripcion (220)')),
                ('ir_a', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Introducción Carrouselle',
                'verbose_name_plural': 'Introducción Carrouselle',
            },
        ),
        migrations.CreateModel(
            name='PreguntasFrecuentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(blank=True, max_length=160, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Preguntas Frecuentes',
                'verbose_name_plural': 'Preguntas Frecuentes',
            },
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='intro_temporada/%Y/%m/%d')),
                ('iframe', models.CharField(blank=True, max_length=600, null=True)),
                ('titulo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Título (40)')),
                ('subtitulo', models.CharField(blank=True, max_length=80, null=True, verbose_name='Subtítulo (80)')),
                ('descripcion', models.CharField(blank=True, max_length=220, null=True, verbose_name='Descripcion (220)')),
            ],
            options={
                'verbose_name': 'Introducción Temporada',
                'verbose_name_plural': 'Introducción Temporada',
            },
        ),
        migrations.CreateModel(
            name='ProductosDestacados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos_destacados_intro/%Y/%m/%d')),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion (150)')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'Introducción Productos Destacados',
                'verbose_name_plural': 'Introducción Productos Destacados',
            },
        ),
        migrations.CreateModel(
            name='AireLibreBeneficios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Título (40)')),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion (220)')),
                ('beneficio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='presentacion.airelibre')),
            ],
        ),
    ]