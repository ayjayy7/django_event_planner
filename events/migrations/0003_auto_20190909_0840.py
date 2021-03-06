# Generated by Django 2.2.5 on 2019-09-09 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_bookevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookevent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bookevent',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bookevent',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='bookevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='bookevent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
