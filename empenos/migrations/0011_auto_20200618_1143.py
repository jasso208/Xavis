# Generated by Django 2.2.6 on 2020-06-18 16:43

import datetime
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empenos', '0010_auto_20200618_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 16, 43, 54, 913516, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 16, 43, 54, 913516, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Retiro_Efectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=7, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 6, 18, 16, 43, 54, 913516, tzinfo=utc))),
                ('importe', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('comentario', models.CharField(default='', max_length=200)),
                ('caja', models.CharField(max_length=1, null=True)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empenos.Sucursal')),
                ('tipo_movimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empenos.Tipo_Movimiento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
