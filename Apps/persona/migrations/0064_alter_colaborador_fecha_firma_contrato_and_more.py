# Generated by Django 4.2 on 2023-07-08 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0063_remove_colaborador_agenda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_firma_contrato',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 16, 31, 59, 630837)),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='fotografia',
            field=models.FileField(blank=True, null=True, upload_to='biolimpieza/static/Images/Colaboradoras/'),
        ),
    ]
