# Generated by Django 2.1.3 on 2018-11-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='Released_Campaigns',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
