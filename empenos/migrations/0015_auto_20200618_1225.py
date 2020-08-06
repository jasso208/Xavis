# Generated by Django 2.2.6 on 2020-06-18 17:25

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empenos', '0014_auto_20200618_1217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genera_Token',
            new_name='Token',
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 17, 25, 17, 41874, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 17, 25, 17, 43875, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 17, 25, 17, 44876, tzinfo=utc)),
        ),
    ]