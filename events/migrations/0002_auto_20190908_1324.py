# Generated by Django 2.2.5 on 2019-09-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
    ]
