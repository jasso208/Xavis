# Generated by Django 2.2.6 on 2020-06-26 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0028_auto_20200626_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 19, 41, 49, 710619)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 19, 41, 49, 717702)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 19, 41, 49, 720709)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 19, 41, 49, 725743)),
        ),
    ]
