# Generated by Django 3.2.6 on 2021-08-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210815_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='myaccount',
            name='industry',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='myaccount',
            name='job_role',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]