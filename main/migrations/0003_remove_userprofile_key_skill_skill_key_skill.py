# Generated by Django 4.2.3 on 2023-07-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_userprofile_name_userprofile_key_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='key_skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='key_skill',
            field=models.BooleanField(default=False),
        ),
    ]