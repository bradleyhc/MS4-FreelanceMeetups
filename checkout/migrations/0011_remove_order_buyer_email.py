# Generated by Django 3.2.6 on 2021-08-19 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20210819_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='buyer_email',
        ),
    ]
