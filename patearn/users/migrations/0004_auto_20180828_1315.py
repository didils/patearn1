# Generated by Django 2.0.8 on 2018-08-28 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180827_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='address',
        ),
    ]
