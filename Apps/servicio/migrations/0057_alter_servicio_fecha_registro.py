# Generated by Django 4.2 on 2023-06-29 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0056_alter_servicio_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fecha_registro',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 29, 10, 54, 50, 542718)),
        ),
    ]
