# Generated by Django 2.2.6 on 2020-07-06 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0054_auto_20200706_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta_empeno',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 17, 23, 228384)),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 17, 23, 137362)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 17, 23, 191376)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_interior',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 17, 23, 140362)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 17, 23, 174372)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 17, 23, 177371)),
        ),
    ]
