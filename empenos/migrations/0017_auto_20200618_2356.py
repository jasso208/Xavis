# Generated by Django 2.2.6 on 2020-06-19 04:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0016_auto_20200618_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='retiro_efectivo',
            name='token',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 4, 56, 4, 867804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 4, 56, 4, 877807, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 4, 56, 4, 885809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 4, 56, 4, 889812, tzinfo=utc)),
        ),
    ]
