# Generated by Django 4.2 on 2023-05-18 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0044_alter_servicio_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fecha_registro',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 18, 6, 25, 2, 660544)),
        ),
    ]
