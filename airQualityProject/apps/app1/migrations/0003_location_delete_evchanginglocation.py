# Generated by Django 4.2.10 on 2024-03-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_evchanginglocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre Sucursal')),
                ('address', models.CharField(max_length=250, verbose_name='Dirección')),
                ('lat', models.FloatField(verbose_name='Latitud')),
                ('lng', models.FloatField(verbose_name='Longitud')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='EVCHangingLocation',
        ),
    ]
