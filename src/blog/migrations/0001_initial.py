# Generated by Django 4.0.4 on 2022-05-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200)),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
            ],
        ),
    ]