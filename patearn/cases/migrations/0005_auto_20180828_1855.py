# Generated by Django 2.0.8 on 2018-08-28 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_auto_20180828_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'ordering': ['-request_date']},
        ),
    ]
