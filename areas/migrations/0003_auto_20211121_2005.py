# Generated by Django 3.2.9 on 2021-11-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_servicearea_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingarea',
            name='center_lat',
            field=models.DecimalField(decimal_places=17, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parkingarea',
            name='center_lng',
            field=models.DecimalField(decimal_places=17, max_digits=20),
        ),
    ]
