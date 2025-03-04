# Generated by Django 5.0.7 on 2025-01-30 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_rename_servicio_venta_servicios'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='venta',
            name='servicios',
        ),
        migrations.AddField(
            model_name='venta',
            name='servicios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.servicio'),
            preserve_default=False,
        ),
    ]
