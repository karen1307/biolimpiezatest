# Generated by Django 4.2 on 2023-05-18 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0027_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 6, 11, 26, 529945)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 6, 11, 26, 528949), null=True),
        ),
    ]
