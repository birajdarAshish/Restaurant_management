# Generated by Django 3.0.4 on 2020-05-01 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20200501_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cost',
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.menu'),
        ),
    ]
