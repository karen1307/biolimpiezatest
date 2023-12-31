# Generated by Django 4.2 on 2023-05-12 23:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicio', '0016_alter_servicio_fecha_registro'),
        ('persona', '0015_alter_colaborador_fecha_firma_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=30)),
                ('nota', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cotizacion', models.DateTimeField(default=datetime.datetime(2023, 5, 12, 18, 41, 48, 849778))),
                ('cliente_cotizante', models.ForeignKey(default=20, on_delete=django.db.models.deletion.SET_DEFAULT, to='persona.clientepersona')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEspacio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('nota', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrestacionServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('detalles_direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('barrio', models.CharField(blank=True, max_length=50, null=True)),
                ('jornada', models.CharField(choices=[('completa', 'Completa'), ('media_am', 'Media en la mañana'), ('media_pm', 'Media en la tarde')], max_length=50)),
                ('fecha_aplicacion', models.DateTimeField(default=datetime.datetime(2023, 5, 12, 18, 41, 48, 849778))),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('aplicado', 'Aplicado'), ('cancelado', 'Cancelado'), ('pendiente_reprogramacion', 'Pendiente de reprog. de fecha'), ('cerrado', 'Cerrado')], default='abierto', max_length=50)),
                ('metros_cuadrados_espacio', models.IntegerField(default=0)),
                ('numero_puestos_trabajo', models.IntegerField(default=0)),
                ('numero_cocinetas', models.IntegerField(default=0)),
                ('numero_banos', models.IntegerField(default=0)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='servicio.municipioservicio')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('profesionales_asignados', models.ManyToManyField(blank=True, null=True, to='persona.colaborador')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='servicio.servicio')),
                ('tipo_espacio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pedido.tipoespacio')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_generacion', models.DateTimeField(default=datetime.datetime(2023, 5, 12, 18, 41, 48, 849778))),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('valor', models.IntegerField(default=0)),
                ('estado', models.CharField(choices=[('pagado', 'Pagado'), ('pendiente_pago', 'Pendiente de pago')], default='pendiente_pago', max_length=30)),
                ('medio_pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='pedido.mediopago')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pedido.pedido')),
            ],
        ),
    ]
