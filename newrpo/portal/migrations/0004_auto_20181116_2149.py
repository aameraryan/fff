# Generated by Django 2.1.3 on 2018-11-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20181116_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='Released_Campaigns',
            field=models.CharField(default='.', max_length=1000),
        ),
    ]
