# Generated by Django 3.1.2 on 2020-10-09 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Waitlist',
            new_name='WaitlistEntry',
        ),
    ]
