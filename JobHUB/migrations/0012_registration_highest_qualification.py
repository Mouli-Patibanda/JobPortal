# Generated by Django 4.2.1 on 2023-06-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHUB', '0011_remove_registration_highest_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Highest_Qualification',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('MCa', 'MCA'), ('BCA', 'BCA'), ('BSC', 'BSC')], default='B.Tech', max_length=6),
        ),
    ]