# Generated by Django 4.2 on 2023-05-05 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0007_alter_registrocontacto_fecha_radicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 5, 17, 53, 988025)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 5, 17, 53, 988025)),
        ),
    ]
