# Generated by Django 4.1.7 on 2023-07-13 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0053_alter_agenda_fecha_alter_factura_fecha_generacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 2, 35, 20, 381357, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 21, 35, 20, 379850)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 12, 21, 35, 20, 377338), null=True),
        ),
    ]
