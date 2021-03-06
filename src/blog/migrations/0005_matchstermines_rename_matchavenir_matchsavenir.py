# Generated by Django 4.0.4 on 2022-05-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_match_matchavenir'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchsTermines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=200)),
                ('championship', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200)),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('nb_yellow_cards', models.IntegerField()),
                ('nb_red_cards', models.IntegerField()),
                ('nb_goals', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='MatchAVenir',
            new_name='MatchsAVenir',
        ),
    ]
