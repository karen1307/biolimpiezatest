# Generated by Django 4.2 on 2023-05-15 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0027_alter_colaborador_fecha_firma_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 21, 37, 0, 426041)),
        ),
    ]