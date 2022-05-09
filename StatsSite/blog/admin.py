from django.contrib import admin
from .models import MatchsAVenir, MatchsTermine


@admin.register(MatchsAVenir)
class MatchAVenir(admin.ModelAdmin):
    list_display = ("date", "match", "championship")
    list_filter = ("date", "championship")


@admin.register(MatchsTermine)
class MatchTermines(admin.ModelAdmin):
    list_display = ("date", "match", "championship", "nb_yellow_cards", "nb_red_cards", "nb_goals")
    list_filter = ("date", "championship")
