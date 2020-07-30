# Generated by Django 2.2.6 on 2020-06-21 23:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empenos', '0018_auto_20200620_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 23, 36, 6, 231926)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 23, 36, 6, 235931)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 23, 36, 6, 237927)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 23, 36, 6, 241931)),
        ),
        migrations.CreateModel(
            name='Aux_Cierra_Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('caja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='empenos.Cajas')),
            ],
        ),
    ]
