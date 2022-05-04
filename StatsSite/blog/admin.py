from django.contrib import admin
from .models import Match


@admin.register(Match)
class Match(admin.ModelAdmin):
    list_display = ("date", "match", "championship")
    list_filter = ("date", "championship")
