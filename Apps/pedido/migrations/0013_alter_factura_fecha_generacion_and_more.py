# Generated by Django 4.2 on 2023-05-15 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0012_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 33, 17, 789932)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 33, 17, 788930)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 33, 17, 789932)),
        ),
    ]