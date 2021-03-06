# Generated by Django 2.0.8 on 2018-08-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20180828_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='application_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='filed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='product_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='products',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='progress_status',
            field=models.CharField(blank=True, choices=[('결제 대기 중', '결제 대기 중'), ('출원 준비 중', '출원 준비 중'), ('심사 중', '심사 중'), ('출원공고', '출원공고'), ('거절 대응 중', '거절 대응 중'), ('등록', '등록'), ('갱신 대상', '갱신 대상')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='publication_date',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='publication_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='registration_date',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='registration_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='trademark_title',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
