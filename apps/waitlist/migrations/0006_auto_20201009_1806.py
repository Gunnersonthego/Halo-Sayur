# Generated by Django 3.1.2 on 2020-10-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0005_auto_20201009_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistentry',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Class Level'),
        ),
    ]
