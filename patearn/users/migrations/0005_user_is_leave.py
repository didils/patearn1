# Generated by Django 2.0.8 on 2018-08-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180828_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_leave',
            field=models.CharField(choices=[('정상 회원', '정상 회원'), ('탈퇴한 회원', '탈퇴한 회원')], max_length=80, null=True),
        ),
    ]