# Generated by Django 4.2 on 2023-05-18 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0039_alter_registrocontacto_fecha_radicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 4, 48, 14, 307995)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 4, 48, 14, 307995)),
        ),
    ]