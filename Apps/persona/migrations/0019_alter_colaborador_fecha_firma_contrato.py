# Generated by Django 4.2 on 2023-05-13 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0018_alter_colaborador_fecha_firma_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 19, 4, 51, 255187)),
        ),
    ]
