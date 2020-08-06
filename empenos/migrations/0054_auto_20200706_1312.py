# Generated by Django 2.2.6 on 2020-07-06 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0053_auto_20200706_1308'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tipo_Pago',
        ),
        migrations.AlterField(
            model_name='boleta_empeno',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 12, 26, 699057)),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 12, 26, 647047)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 12, 26, 675052)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 12, 26, 651045)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 12, 26, 657049)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 13, 12, 26, 659048)),
        ),
    ]