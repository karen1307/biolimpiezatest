# Generated by Django 4.2 on 2023-07-02 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0058_alter_registrocontacto_fecha_radicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 1, 21, 53, 2, 747318)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 21, 53, 2, 747318)),
        ),
    ]
