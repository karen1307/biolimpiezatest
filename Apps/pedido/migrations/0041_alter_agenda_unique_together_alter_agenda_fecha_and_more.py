# Generated by Django 4.2 on 2023-06-29 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0040_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 10, 30, 47, 676180)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 10, 30, 47, 676180)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 10, 30, 47, 665754), null=True),
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('fecha', 'prestacion_servicio', 'jornada')},
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='profesional',
        ),
    ]
