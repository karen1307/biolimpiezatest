# Generated by Django 4.2 on 2023-07-12 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0066_alter_colaborador_fecha_firma_contrato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='autorizacion_imagen_publica',
            field=models.FileField(blank=True, null=True, upload_to='static/Documentos/autorizaciones_imagen_publica/'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 16, 56, 11, 685136)),
        ),
    ]
