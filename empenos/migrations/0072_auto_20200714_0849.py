# Generated by Django 2.2.6 on 2020-07-14 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0071_auto_20200713_2004'),
    ]

    operations = [        
        migrations.AlterField(
            model_name='boleta_empeno',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 8, 49, 34, 471847)),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 8, 49, 34, 436837)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 8, 49, 34, 467845)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 8, 49, 34, 447841)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 8, 49, 34, 449839)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 8, 49, 34, 452840)),
        ),
    ]