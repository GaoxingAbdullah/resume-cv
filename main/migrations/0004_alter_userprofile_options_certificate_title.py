# Generated by Django 4.2.3 on 2023-07-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_userprofile_key_skill_skill_key_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profiles', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AddField(
            model_name='certificate',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]