# Generated by Django 3.2 on 2022-07-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorreoArgentino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable_inscripto_domicilio', models.TextField(default='')),
                ('responsable_inscripto_sucursal', models.TextField(default='', null=True, verbose_name='Monotributista y Consumidor Final')),
                ('url', models.CharField(default='https://www.correoargentino.com.ar/MiCorreo/public/faqs', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PreciosRISucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_1', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_2', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_3', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_4', models.DecimalField(decimal_places=2, max_digits=12)),
                ('correo_argentino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transporte.correoargentino')),
            ],
            options={
                'verbose_name': 'Precios Responsable Inscripto a Sucursal',
                'verbose_name_plural': 'Precios Responsable Inscripto a Sucursal',
            },
        ),
        migrations.CreateModel(
            name='PreciosRIDomicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_1', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_2', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_3', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_4', models.DecimalField(decimal_places=2, max_digits=12)),
                ('correo_argentino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transporte.correoargentino')),
            ],
            options={
                'verbose_name': 'Precios Responsable Inscripto a Domicilio',
                'verbose_name_plural': 'Precios Responsable Inscripto a Domicilio',
            },
        ),
        migrations.CreateModel(
            name='PreciosMCFSucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_1', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_2', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_3', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_4', models.DecimalField(decimal_places=2, max_digits=12)),
                ('correo_argentino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transporte.correoargentino')),
            ],
            options={
                'verbose_name': 'Precios Monotributista y Consumidor Final a Sucursal',
                'verbose_name_plural': 'Precios Monotributista y Consumidor Final a Sucursal',
            },
        ),
        migrations.CreateModel(
            name='PreciosMCFDomicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_1', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_2', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_3', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zona_4', models.DecimalField(decimal_places=2, max_digits=12)),
                ('correo_argentino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transporte.correoargentino')),
            ],
            options={
                'verbose_name': 'Precios Monotributista y Consumidor Final a Domicilio',
                'verbose_name_plural': 'Precios Monotributista y Consumidor Final a Domicilio',
            },
        ),
    ]