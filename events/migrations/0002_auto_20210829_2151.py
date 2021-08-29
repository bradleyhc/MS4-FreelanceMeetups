# Generated by Django 3.2.6 on 2021-08-29 21:51

from django.conf import settings
from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='event',
            name='max_reg',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='event',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(choices_display='WITH_GMT_OFFSET', default='Europe/London'),
        ),
        migrations.AlterField(
            model_name='event',
            name='industry',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='Online', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='registrants',
            field=models.ManyToManyField(blank=True, related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
    ]
