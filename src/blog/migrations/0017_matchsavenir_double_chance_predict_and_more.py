# Generated by Django 4.0.4 on 2022-05-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_matchsavenir_away_team_cards_against_average_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchsavenir',
            name='double_chance_predict',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchstermine',
            name='double_chance_predict',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]