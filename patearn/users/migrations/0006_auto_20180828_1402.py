# Generated by Django 2.0.8 on 2018-08-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='applicant_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cumulative_pay_amount',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cumulative_usage_count',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_leave',
            field=models.CharField(blank=True, choices=[('정상 회원', '정상 회원'), ('탈퇴한 회원', '탈퇴한 회원')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='note',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='postalcode',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='push_token',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='signature_image',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='social_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
