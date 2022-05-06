from django.db import models
from django.urls import reverse


class Match(models.Model):
    match = models.CharField(max_length=200)
    championship = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)

    def __str__(self):
        return self.match.replace("|", " - ")

    def get_absolute_url(self):
        return reverse("blog-match_detail", kwargs={"slug": self.slug})



