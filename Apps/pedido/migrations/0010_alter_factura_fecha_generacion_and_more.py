# Generated by Django 4.2 on 2023-05-15 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 22, 42, 807531)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 22, 42, 806531)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 22, 42, 806531)),
        ),
    ]
