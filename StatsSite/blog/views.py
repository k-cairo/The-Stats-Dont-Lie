from django.shortcuts import render, HttpResponse
from pathlib import Path
from constant import LOGO_LIST
import os
import json

BASE_DIRECTORY = Path(__file__).resolve().parent.parent.parent


def index(request):
    json_file = os.path.join(BASE_DIRECTORY, "Liste de Matchs/02-05-2022.json")
    with open(json_file, "r") as f:
        match_list = json.load(f)
    context = {"matchs": match_list, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def match_detail(request, slug):
    return render(request, "blog/stats_details.html", context={"slug": slug})