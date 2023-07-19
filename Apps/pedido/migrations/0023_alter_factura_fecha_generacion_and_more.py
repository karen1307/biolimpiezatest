# Generated by Django 4.2 on 2023-05-18 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0022_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 3, 47, 1, 325719)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 3, 47, 1, 325719), null=True),
        ),
    ]
