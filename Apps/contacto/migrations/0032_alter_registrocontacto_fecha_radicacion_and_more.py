# Generated by Django 4.2 on 2023-05-15 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0031_alter_registrocontacto_fecha_radicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 4, 20, 11, 201824)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 4, 20, 11, 201824)),
        ),
    ]
