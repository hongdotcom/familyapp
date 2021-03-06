# Generated by Django 3.1.5 on 2021-01-17 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('familyevent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsupply',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.RESTRICT, related_name='supply', to='familyevent.familyevent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventsupply',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='eventsupply',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='eventsupply',
            name='prepared',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='supply', to=settings.AUTH_USER_MODEL),
        ),
    ]
