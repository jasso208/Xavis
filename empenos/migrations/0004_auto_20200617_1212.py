# Generated by Django 2.2.6 on 2020-06-17 17:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empenos', '0003_auto_20200617_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 17, 11, 58, 57235, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Sucursales_Regional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empenos.Sucursal')),
            ],
        ),
    ]
