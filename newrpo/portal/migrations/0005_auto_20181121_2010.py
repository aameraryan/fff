# Generated by Django 2.1.3 on 2018-11-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20181116_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='Company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='prospect',
            name='Emp_Size',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
