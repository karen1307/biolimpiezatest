# Generated by Django 4.2 on 2023-05-12 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 18, 56, 38, 628185)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 18, 56, 38, 628185)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 18, 56, 38, 628185)),
        ),
    ]