# Generated by Django 4.2.1 on 2023-06-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0038_remove_jobcreate_mobile'),
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
        migrations.AlterField(
            model_name='jobcreate',
            name='username',
            field=models.CharField(max_length=20),
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
