# Generated by Django 4.2 on 2023-05-13 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0023_alter_bono_options_alter_estadoservicio_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fecha_registro',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 12, 21, 10, 49, 504388)),
        ),
    ]