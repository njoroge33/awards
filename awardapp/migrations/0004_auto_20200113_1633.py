# Generated by Django 3.0.2 on 2020-01-13 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0003_auto_20200113_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_url',
            new_name='project_link',
        ),
    ]
