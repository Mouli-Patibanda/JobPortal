# Generated by Django 4.2.1 on 2023-06-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0019_registration_highest_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='pdf_file',
            field=models.FileField(default='default.pdf', upload_to='documents/{Resume}/'),
        ),
    ]