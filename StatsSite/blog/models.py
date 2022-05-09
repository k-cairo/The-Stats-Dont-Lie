from django.db import models
from django.urls import reverse


class MatchsAVenir(models.Model):
    match = models.CharField(max_length=200)
    championship = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    nb_yellow_cards = models.IntegerField(blank=True, null=True)
    nb_red_cards = models.IntegerField(blank=True, null=True)
    nb_goals = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.match.replace("|", " - ")

    def get_absolute_url(self):
        return reverse("blog-match_detail", kwargs={"slug": self.slug})


class MatchsTermine(models.Model):
    match = models.CharField(max_length=200)
    championship = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    nb_yellow_cards = models.IntegerField()
    nb_red_cards = models.IntegerField()
    nb_goals = models.IntegerField()

    def __str__(self):
        return self.match.replace("|", " - ")

    def get_absolute_url(self):
        return reverse("blog-match_detail", kwargs={"slug": self.slug})



