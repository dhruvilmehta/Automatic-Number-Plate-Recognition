# Generated by Django 3.2.9 on 2022-05-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydetection', '0002_rename_image_image_numberimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='numberplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number', models.IntegerField(default=0)),
            ],
        ),
    ]
