# Generated by Django 5.1.3 on 2024-11-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('bid', models.CharField(max_length=20, primary_key='bid', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('interst', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
