# Generated by Django 4.2.1 on 2023-06-21 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0016_registration_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Highest_Qualification',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='pdf_file',
        ),
    ]
