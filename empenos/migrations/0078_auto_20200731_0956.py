# Generated by Django 2.2.6 on 2020-07-31 09:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0077_auto_20200728_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abono',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='abono',
            name='caja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empenos.Cajas'),
        ),
        migrations.AlterField(
            model_name='abono',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 453034)),
        ),
        migrations.AlterField(
            model_name='boleta_empeno',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 438028)),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 411384)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 435029)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 419388)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 421387)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 56, 45, 422389)),
        ),
    ]
