# Generated by Django 3.2 on 2023-07-09 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='address',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='name',
        ),
    ]
