# Generated by Django 3.2.9 on 2022-05-05 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydetection', '0005_auto_20220505_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplate',
            name='timestampin',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='numberplate',
            name='timestampout',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
