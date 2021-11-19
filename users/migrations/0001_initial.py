# Generated by Django 3.2.9 on 2021-11-19 21:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=16)),
                ('role', models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='users.role')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
