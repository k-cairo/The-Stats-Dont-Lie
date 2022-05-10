# Generated by Django 4.0.4 on 2022-05-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_match_championship'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='nb_goals',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='nb_red_cards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='nb_yellow_cards',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]