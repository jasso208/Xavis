# Generated by Django 2.2.4 on 2019-09-16 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0010_e_mail_notificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recupera_pws',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=18)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
