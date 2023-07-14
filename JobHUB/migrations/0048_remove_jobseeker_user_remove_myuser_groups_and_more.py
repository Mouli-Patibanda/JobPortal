# Generated by Django 4.2.1 on 2023-06-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0047_remove_jobseeker_user_remove_myuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='user',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='jobcreate',
            name='username',
            field=models.CharField(blank=True, default='James', max_length=20, null=True),
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
