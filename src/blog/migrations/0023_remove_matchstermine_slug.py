# Generated by Django 4.0.4 on 2022-05-21 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_remove_matchstermine_championship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchstermine',
            name='slug',
        ),
    ]