# Generated by Django 4.2 on 2023-05-18 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0031_alter_clienteempresa_identidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 3, 17, 34, 995888)),
        ),
    ]
