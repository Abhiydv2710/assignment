# Generated by Django 3.2.8 on 2021-11-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=20)),
                ('middlename', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('movies', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=100)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
