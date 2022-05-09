from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ...get_matchs import format_championships_names, format_teams_names
from .constant2 import LOGO_LIST, LIST_CHAMPIONSHIP
from .models import MatchsAVenir, MatchsTermine
import os
import json
from slugify import slugify
from datetime import datetime, timedelta, date
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

BASE_DIRECTORY = Path(__file__).resolve().parent.parent.parent

today = datetime.today().strftime("%d-%m-%Y")
tomorrow = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
j2 = (date.today() + timedelta(days=2)).strftime("%d-%m-%Y")
j3 = (date.today() + timedelta(days=3)).strftime("%d-%m-%Y")
j4 = (date.today() + timedelta(days=4)).strftime("%d-%m-%Y")
j5 = (date.today() + timedelta(days=5)).strftime("%d-%m-%Y")

day_list = (today, tomorrow, j2, j3, j4, j5)


def open_browser():
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except:
        service = Service(executable_path="./chromedriver/chromedriver.exe")
    finally:
        driver = webdriver.Chrome(service=service)
    return driver


def accept_cookie(driver):
    try:
        driver.implicitly_wait(1)
        frame = driver.find_element(By.XPATH, '//*[@id="appconsent"]/iframe')
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[1]/button/span').click()
        driver.switch_to.default_content()
    except NoSuchElementException:
        pass
    finally:
        pass


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
                        get_match_stats(match=format_match, championship=championship_format, date=date,
                                        url=match_href)

    return HttpResponse("Matchs finish Update")


def get_match_stats(championship, match, date, url):
    driver = open_browser()
    driver.get(url)

    nb_goals = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement1"))
    nb_yellow_cards = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement4"))
    nb_red_cards = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement3"))

    new_query = MatchsAVenir.objects.filter(date=date, match=match.replace("|", " - "))

    if len(new_query) != 0:
        new_query_values = new_query.values()

        query_match = new_query_values[0]['match']
        query_championship = new_query_values[0]['championship']
        query_date = new_query_values[0]['date']
        query_slug = new_query_values[0]['slug']
        query_home_team = new_query_values[0]['home_team']
        query_away_team = new_query_values[0]['away_team']

        MatchsTermines.objects.create(match=new_query_values[0]['match'],
                                      championship=new_query_values[0]['championship'],
                                      date=new_query_values[0]['date'],
                                      slug=new_query_values[0]['slug'],
                                      home_team=new_query_values[0]['home_team'],
                                      away_team=new_query_values[0]['away_team'],
                                      nb_yellow_cards=nb_yellow_cards,
                                      nb_red_cards=nb_red_cards,
                                      nb_goals=nb_goals)

        MatchsAVenir.objects.filter(date=date, match=match.replace("|", " - ")).delete()


def index(request):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    context = {"matchs": today_j3_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def match_detail(request, slug):
    match = get_object_or_404(MatchsAVenir, slug=slug)
    return render(request, "blog/stats_details.html", context={"match": match})
