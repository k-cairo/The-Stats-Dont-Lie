from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from pathlib import Path
from .constant2 import LOGO_LIST
from .models import Match
import os
import json
from slugify import slugify
from datetime import datetime, timedelta, date
from django.db.models import Q

BASE_DIRECTORY = Path(__file__).resolve().parent.parent.parent

today = datetime.today().strftime("%d-%m-%Y")
tomorrow = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
j2 = (date.today() + timedelta(days=2)).strftime("%d-%m-%Y")
j3 = (date.today() + timedelta(days=3)).strftime("%d-%m-%Y")
j4 = (date.today() + timedelta(days=4)).strftime("%d-%m-%Y")
j5 = (date.today() + timedelta(days=5)).strftime("%d-%m-%Y")

day_list = (today, tomorrow, j2, j3, j4, j5)


def add_match_into_database():
    for day in day_list:
        json_file = os.path.join(BASE_DIRECTORY, f"Liste de Matchs/{day}.json")
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                match_list = json.load(f)

        for date, date_matchs in match_list.items():
            for championship, rencontres in date_matchs.items():
                for rencontre in rencontres:
                    if not Match.objects.filter(match=rencontre.replace('|', ' - '), date=date).exists():
                        Match.objects.create(match=rencontre.replace('|', ' - '),
                                             championship=championship,
                                             date=date,
                                             slug=slugify(rencontre),
                                             home_team=rencontre.split("|")[0],
                                             away_team=rencontre.split("|")[1])


def index(request):
    add_match_into_database()
    today_j3_matchs = Match.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    context = {"matchs": today_j3_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def match_detail(request, slug):
    match = get_object_or_404(Match, slug=slug)
    return render(request, "blog/stats_details.html", context={"match": match})

