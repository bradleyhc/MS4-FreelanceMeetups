# Generated by Django 3.2.5 on 2021-07-29 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_myaccount_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myaccount',
            name='password',
        ),
    ]