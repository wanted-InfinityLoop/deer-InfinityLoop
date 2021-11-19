# Generated by Django 3.2.9 on 2021-11-19 17:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('charges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'units',
            },
        ),
        migrations.CreateModel(
            name='DiscountOrPenalties',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=32)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='charges.type')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='charges.unit')),
            ],
            options={
                'db_table': 'discount_or_penalties',
            },
        ),
    ]
