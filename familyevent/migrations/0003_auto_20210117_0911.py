# Generated by Django 3.1.5 on 2021-01-17 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familyevent', '0002_auto_20210117_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsupply',
            old_name='eventdate',
            new_name='updated_date',
        ),
    ]
