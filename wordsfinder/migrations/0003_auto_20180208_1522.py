# Generated by Django 2.0.2 on 2018-02-08 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordsfinder', '0002_auto_20180208_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='word',
            new_name='words',
        ),
    ]
