# Generated by Django 4.2 on 2023-07-08 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0065_alter_colaborador_fecha_firma_contrato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 17, 25, 49, 685443)),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='fotografia',
            field=models.FileField(blank=True, null=True, upload_to='static/Images/Colaboradoras/'),
        ),
    ]
