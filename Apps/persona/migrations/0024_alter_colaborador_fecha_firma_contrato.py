# Generated by Django 4.2 on 2023-05-15 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0023_alter_administrador_options_alter_arl_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 22, 42, 803435)),
        ),
    ]
