# Generated by Django 3.1.5 on 2021-01-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyevent', '0003_auto_20210117_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsupply',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='eventsupply',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
