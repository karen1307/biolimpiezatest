# Generated by Django 4.1.5 on 2023-04-28 20:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoBeneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio_jornada_am', models.IntegerField()),
                ('precio_jornada_pm', models.IntegerField()),
                ('precio_jornada_completa', models.IntegerField()),
                ('precio_hora_adicional', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('fecha_registro', models.DateTimeField(verbose_name=datetime.datetime(2023, 4, 28, 15, 48, 14, 228388))),
                ('tipo_equipo', models.CharField(choices=[('individual', 'Individual (1 colaborador)'), ('colectivo', 'Colectivo (Más de 1 colaborador)')], max_length=50)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='servicio.estadoservicio')),
            ],
        ),
        migrations.CreateModel(
            name='MunicipioServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('zona_ubicacion', models.CharField(choices=[('centro', 'Zona centro'), ('norte', 'Zona norte'), ('sur', 'Zona sur'), ('oriental', 'Zona oriental')], max_length=20)),
                ('costo_transporte', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='servicio.estadoservicio')),
            ],
        ),
        migrations.CreateModel(
            name='Bono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('porcentaje_descuento', models.IntegerField()),
                ('jornada', models.CharField(choices=[('completa', 'Completa'), ('media_am', 'Media en la mañana'), ('media_pm', 'Media en la tarde')], max_length=50)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.grupobeneficiario')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.servicio')),
            ],
        ),
    ]