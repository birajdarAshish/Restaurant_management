# Generated by Django 3.0.4 on 2020-05-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20200429_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='nope', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='contact_no',
            field=models.CharField(default='+91', max_length=13),
            preserve_default=False,
        ),
    ]
