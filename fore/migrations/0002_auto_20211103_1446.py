# Generated by Django 3.2.8 on 2021-11-03 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regi',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='regi',
            name='movies',
        ),
    ]
