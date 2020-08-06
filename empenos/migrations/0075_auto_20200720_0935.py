# Generated by Django 2.2.6 on 2020-07-20 09:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empenos', '0074_auto_20200714_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta_empeno',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 9, 35, 42, 458715)),
        ),
        migrations.AlterField(
            model_name='cajas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 9, 35, 42, 417705)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 9, 35, 42, 455715)),
        ),
        migrations.AlterField(
            model_name='otros_ingresos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 9, 35, 42, 419705)),
        ),
        migrations.AlterField(
            model_name='retiro_efectivo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 9, 35, 42, 420705)),
        ),
        migrations.AlterField(
            model_name='token',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 9, 35, 42, 423709)),
        ),
        migrations.CreateModel(
            name='Pagos_Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.DateTimeField()),
                ('almacenaje', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('interes', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('importe', models.IntegerField()),
                ('vencido', models.CharField(default='N', max_length=1)),
                ('pagado', models.CharField(default='N', max_length=1)),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('boleta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='empenos.Boleta_Empeno')),
                ('tipo_pago', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='empenos.Tipo_Pago')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]