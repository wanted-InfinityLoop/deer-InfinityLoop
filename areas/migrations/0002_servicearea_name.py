# Generated by Django 3.2.9 on 2021-11-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicearea',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
    ]