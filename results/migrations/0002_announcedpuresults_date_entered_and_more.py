# Generated by Django 5.0.2 on 2024-08-12 08:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcedpuresults',
            name='date_entered',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='announcedpuresults',
            name='entered_by_user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='announcedpuresults',
            name='user_ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
