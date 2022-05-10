from django.shortcuts import render, HttpResponse
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utils.constant import LOGO_LIST, LIST_CHAMPIONSHIP
from utils.get_matchs import format_championships_names, format_teams_names
from utils.selenium_functions import open_browser, accept_cookie
from utils.get_matchs_cards_goals import get_matchs_cards_goals
from utils.get_cards_iframes import get_all_cards_iframes
from .models import MatchsAVenir, Data, Iframe
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


################################################   INDEX   #############################################################
def index(request):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    context = {"matchs": today_j3_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


############################################   UPDATE MATCHS   #########################################################
def update_matchs_a_venir(request):
    for day in day_list:
        json_file = os.path.join(BASE_DIRECTORY, f"Liste de Matchs/{day}.json")
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                match_list = json.load(f)
        for date, date_matchs in match_list.items():
            for championship, rencontres in date_matchs.items():
                for rencontre in rencontres:
                    if not MatchsAVenir.objects.filter(match=rencontre.replace('|', ' - '), date=date).exists():
                        MatchsAVenir.objects.create(match=rencontre.replace('|', ' - '),
                                                    championship=championship,
                                                    date=date,
                                                    slug=slugify(rencontre),
                                                    home_team=rencontre.split("|")[0],
                                                    away_team=rencontre.split("|")[1])
    return HttpResponse("Matchs list Update")


def update_matchs_termines(request):
    driver = open_browser()
    dates_to_update = []
    all_matchs = MatchsAVenir.objects.all()
    for match in all_matchs:
        if match.date < today:
            if match.date not in dates_to_update:
                dates_to_update.append(match.date)
    for date in dates_to_update:
        driver.get(f"https://www.matchendirect.fr/resultat-foot-{date}/")

        accept_cookie(driver=driver)

        all_div_championships = driver.find_elements(By.CSS_SELECTOR, "div div.panel.panel-info")

        for div_championship in all_div_championships[:-2]:
            try:
                championship = div_championship.find_element(By.CSS_SELECTOR, "h3.panel-title a").text
            except NoSuchElementException:
                print("Problème avec un Championnat")
            else:
                if championship in LIST_CHAMPIONSHIP:
                    championship_format = format_championships_names(championship=championship)
                    raw_matchs = div_championship.find_elements(By.CSS_SELECTOR, "tbody td.lm3")
                    for row_match in raw_matchs:
                        home_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq1").text
                        home_team_format = format_teams_names(team=home_team)
                        away_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq2").text
                        away_team_format = format_teams_names(team=away_team)
                        match_href = row_match.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                        format_match = f"{home_team_format}|{away_team_format}"
                        get_matchs_cards_goals(match=format_match, date=date,
                                        url=match_href)
    return HttpResponse("Matchs finish Update")


########################################   UPDATE CARDS IFRAMES   ######################################################
def update_iframes(request):
    """
    Save Iframes into Database
    :param request:
    :return: HttpResponse
    """
    iframes = get_all_cards_iframes()

    for championship, iframe in iframes[0]:
        Iframe.objects.create(championship=championship, iframe_url=iframe,
                              iframe_stats="cards for", date_updated=today)

    for championship, iframe in iframes[1]:
        Iframe.objects.create(championship=championship, iframe_url=iframe,
                              iframe_stats="cards against", date_updated=today)

    return HttpResponse("Iframes Update")


############################################   UPDATE DATAS   ##########################################################
def update_datas(request):
    return HttpResponse("Datas Update")


