from django.contrib import admin
from .models import MatchsAVenir, MatchsTermine, Iframe, Data, TeamIframe


@admin.register(MatchsAVenir)
class MatchAVenir(admin.ModelAdmin):
    list_display = ("date", "match", "championship", "card_bet", "double_chance_predict")
    list_filter = ("date", "championship", "card_bet")
    search_fields = ("championship", "home_team", "away_team")


@admin.register(MatchsTermine)
class MatchTermines(admin.ModelAdmin):
    list_display = ("target_team", )


@admin.register(Iframe)
class Iframe(admin.ModelAdmin):
    list_display = ("championship", "iframe_url", "iframe_stats", "date_updated")


@admin.register(Data)
class Data(admin.ModelAdmin):
    list_display = ('championship', 'datas', "datas_stats", "date_updated")


@admin.register(TeamIframe)
class Data(admin.ModelAdmin):
    list_display = ("team", "iframe_url", "iframe_stats", "date_updated")