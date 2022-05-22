from datetime import date
from django.db import models
from django.urls import reverse


class MatchsAVenir(models.Model):
    match = models.CharField(max_length=200)
    championship = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_team_cards_for_average = models.FloatField()
    away_team_cards_for_average = models.FloatField()
    home_team_cards_against_average = models.FloatField()
    away_team_cards_against_average = models.FloatField()
    card_bet = models.CharField(max_length=10)
    double_chance_predict = models.CharField(max_length=10)

    def __str__(self):
        return self.match.replace("|", " - ")

    def get_absolute_url(self):
        return reverse("blog-match_detail", kwargs={"slug": self.slug})


class MatchsTermine(models.Model):
    target_team = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    home_team = models.CharField(max_length=100)
    score = models.CharField(max_length=20)
    away_team = models.CharField(max_length=100)
    corner_for = models.IntegerField()
    corner_against = models.IntegerField()
    yellow_card_for = models.IntegerField()
    yellow_card_against = models.IntegerField()
    red_card_for = models.IntegerField()
    red_card_against = models.IntegerField()

    def __str__(self):
        return f"{self.home_team} - {self.away_team}"



class Iframe(models.Model):
    championship = models.CharField(max_length=200)
    iframe_url = models.URLField()
    iframe_stats = models.CharField(max_length=200)
    date_updated = models.CharField(max_length=200)


class TeamIframe(models.Model):
    team = models.CharField(max_length=200)
    iframe_url = models.URLField()
    iframe_stats = models.CharField(max_length=200)
    date_updated = models.CharField(max_length=200)


class Data(models.Model):
    championship = models.CharField(max_length=200)
    datas = models.JSONField()
    datas_stats = models.CharField(max_length=200)
    date_updated = models.CharField(max_length=200)






