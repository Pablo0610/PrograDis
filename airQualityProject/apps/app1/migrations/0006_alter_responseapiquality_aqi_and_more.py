# Generated by Django 4.2.10 on 2024-03-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_responseapiquality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseapiquality',
            name='aqi',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='responseapiquality',
            name='blue',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='responseapiquality',
            name='coSource',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='responseapiquality',
            name='green',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='responseapiquality',
            name='noValue',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='responseapiquality',
            name='pm10Value',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='responseapiquality',
            name='red',
            field=models.TextField(max_length=100),
        ),
    ]
