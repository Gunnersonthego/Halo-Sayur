# Generated by Django 3.1.2 on 2020-10-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0004_waitlistentry_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistentry',
            name='level',
            field=models.IntegerField(verbose_name='Class Level'),
        ),
    ]
