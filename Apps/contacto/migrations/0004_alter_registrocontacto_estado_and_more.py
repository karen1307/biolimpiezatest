# Generated by Django 4.2 on 2023-05-05 08:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_alter_registrocontacto_fecha_radicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocontacto',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='contacto.estadoregistrocontacto'),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_radicacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 3, 12, 10, 951902)),
        ),
        migrations.AlterField(
            model_name='registrocontacto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 3, 12, 10, 951902)),
        ),
    ]
