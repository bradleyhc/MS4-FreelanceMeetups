# Generated by Django 3.2.5 on 2021-07-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_myaccount_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='myaccount',
            name='username',
            field=models.CharField(default='def_username', max_length=60, unique=True),
        ),
    ]