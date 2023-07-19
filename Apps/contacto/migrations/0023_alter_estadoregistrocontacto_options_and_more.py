# Generated by Django 4.2 on 2023-05-13 00:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0022_alter_estadoregistrocontacto_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estadoregistrocontacto',
            options={'verbose_name': 'Estado de registro de contacto', 'verbose_name_plural': 'Estados de registro de contacto'},
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 19, 37, 21, 12817)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 27, 19, 37, 21, 12817)),
        ),
    ]
