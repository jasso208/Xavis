# Generated by Django 2.2.6 on 2020-01-26 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0043_remove_productos_publicado_ml'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estatus_publicacion',
        ),
    ]