# Generated by Django 4.2.1 on 2023-06-23 14:50

import JobHUB.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0039_remove_jobseeker_user_remove_myuser_groups_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='jobseeker',
        #     name='user',
        # ),
        # migrations.RemoveField(
        #     model_name='myuser',
        #     name='groups',
        # ),
        # migrations.RemoveField(
        #     model_name='myuser',
        #     name='user_permissions',
        # ),
        migrations.AddField(
            model_name='jobcreate',
            name='mobile',
            field=models.CharField(default=JobHUB.models.calculate_default_mobile, max_length=10),
        ),
        # migrations.DeleteModel(
        #     name='company',
        # ),
        # migrations.DeleteModel(
        #     name='jobseeker',
        # ),
        # migrations.DeleteModel(
        #     name='MyUser',
        # ),
    ]
