# Generated by Django 4.2 on 2023-05-15 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0031_alter_servicio_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fecha_registro',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 15, 4, 20, 11, 186196)),
        ),
    ]
