# Generated by Django 4.2 on 2023-06-29 15:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0054_alter_colaborador_fecha_firma_contrato'),
        ('pedido', '0039_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 10, 16, 11, 940473)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 10, 16, 11, 940473), null=True),
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 6, 29, 10, 16, 11, 940473))),
                ('jornada', models.CharField(choices=[('completa', 'Completa'), ('media_am', 'Media en la mañana'), ('media_pm', 'Media en la tarde')], default='completa', max_length=50)),
                ('prestacion_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.prestacionservicio')),
                ('profesional', models.ForeignKey(default=20, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Profesional', to='persona.colaborador')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
                'unique_together': {('fecha', 'profesional', 'jornada')},
            },
        ),
    ]
