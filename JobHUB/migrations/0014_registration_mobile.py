# Generated by Django 4.2.1 on 2023-06-20 03:30

import JobHUB.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0013_remove_registration_highest_qualification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='mobile',
            field=models.CharField(default=JobHUB.models.calculate_default_mobile, max_length=10),
        ),
    ]
