# Generated by Django 2.2.6 on 2020-06-17 04:48

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empenos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 4, 48, 43, 741231, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='user_2',
            unique_together={('user',)},
        ),
    ]
