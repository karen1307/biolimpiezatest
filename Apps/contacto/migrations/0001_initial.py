# Generated by Django 4.1.5 on 2023-04-28 20:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoRegistroContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('prioridad', models.CharField(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('mensaje', models.TextField()),
                ('fecha_radicacion', models.DateTimeField(default=datetime.datetime(2023, 4, 28, 15, 48, 14, 226394))),
                ('fecha_vencimiento', models.DateTimeField(default=datetime.datetime(2023, 5, 13, 15, 48, 14, 226394))),
                ('fecha_respuesta', models.DateTimeField()),
                ('respuesta', models.TextField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contacto.estadoregistrocontacto')),
                ('tipo_mensaje', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contacto.tipomensaje')),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contacto.tipousuario')),
                ('usuario_responsable_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
