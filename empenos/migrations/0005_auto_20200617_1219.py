# Generated by Django 2.2.6 on 2020-06-17 17:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0004_auto_20200617_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sucursales_regional',
            old_name='id_usuario',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 17, 19, 33, 902252, tzinfo=utc)),
        ),
    ]