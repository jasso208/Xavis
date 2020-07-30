# Generated by Django 2.2.6 on 2020-07-14 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0073_auto_20200714_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='fecha_pago',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boleta_empeno',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 12, 54, 990619)),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 12, 54, 966612)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 12, 54, 987619)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 12, 54, 971614)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 12, 54, 973614)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 9, 12, 54, 975619)),
        ),
    ]
