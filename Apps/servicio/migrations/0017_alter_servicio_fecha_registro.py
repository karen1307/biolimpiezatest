# Generated by Django 4.2 on 2023-05-12 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0016_alter_servicio_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fecha_registro',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 12, 18, 44, 0, 617359)),
        ),
    ]