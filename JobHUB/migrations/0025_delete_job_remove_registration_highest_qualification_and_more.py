# Generated by Django 4.2.1 on 2023-06-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0024_myuser_delete_job'),
    ]

    operations = [
        # migrations.DeleteModel(
        #     name='Job',
        # ),
        migrations.RemoveField(
            model_name='registration',
            name='Highest_Qualification',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='pdf_file',
        ),
    ]