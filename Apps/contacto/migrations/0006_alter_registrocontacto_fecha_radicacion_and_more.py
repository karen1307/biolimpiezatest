# Generated by Django 4.2 on 2023-05-05 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0005_alter_registrocontacto_fecha_radicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 3, 38, 41, 273370)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 3, 38, 41, 273370)),
        ),
    ]