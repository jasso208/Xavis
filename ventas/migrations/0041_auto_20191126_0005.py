# Generated by Django 2.2.6 on 2019-11-26 06:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0040_auto_20191113_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion_envio_venta',
            name='colonia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 6, 5, 43, 816973, tzinfo=utc)),
        ),
    ]