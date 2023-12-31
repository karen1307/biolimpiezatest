# Generated by Django 4.2 on 2023-07-08 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0048_alter_agenda_unique_together_alter_agenda_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 7, 8, 21, 2, 34, 952999, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_generacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 16, 2, 34, 952999)),
        ),
        migrations.AlterField(
            model_name='prestacionservicio',
            name='fecha_aplicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 8, 16, 2, 34, 952999), null=True),
        ),
    ]
