from django.shortcuts import render, HttpResponse
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utils.constant import LOGO_LIST, LIST_CHAMPIONSHIP
from utils.get_data import get_data
from utils.get_matchs import format_championships_names, format_teams_names, day_list, today, tomorrow, j2, \
    get_all_matchs, get_matchs_cards_goals
from utils.selenium_functions import open_browser, accept_cookie
from utils.get_cards_iframes import get_all_cards_iframes
from .models import MatchsAVenir, Data, Iframe
from django.db.models import Q
from slugify import slugify

BASE_DIRECTORY = Path(__file__).resolve().parent.parent.parent


################################################   INDEX   #############################################################
def index(request):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    context = {"matchs": today_j3_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


############################################   MATCH DETAILS   #########################################################
# TODO
def match_details(request, slug):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    for match in today_j3_matchs:
        if match.slug == slug:
            target_match = match
    return render(request, "blog/match_details.html", context={"match": target_match})


########################################   UPDATE MATCHS A VENIR   #####################################################
def update_matchs_a_venir(request):
    # Check if day already in database (Next 5 days)
    for day in day_list:
        data_dates = MatchsAVenir.objects.filter(date=day)
        if len(data_dates) == 0:
            all_matchs = get_all_matchs(day)

            for championship, rencontres in all_matchs.items():
                for rencontre in rencontres:
                    if not MatchsAVenir.objects.filter(match=rencontre.replace('|', ' - '), date=day).exists():
                        MatchsAVenir.objects.create(match=rencontre.replace('|', ' - '),
                                                    championship=championship,
                                                    date=day,
                                                    slug=slugify(rencontre),
                                                    home_team=rencontre.split("|")[0],
                                                    away_team=rencontre.split("|")[1])
    return HttpResponse("Matchs list Update")


#########################################   UPDATE STATS MATCHS   ######################################################
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
    iframes = get_all_cards_iframes()

    for championship, iframe in iframes[0].items():
        Iframe.objects.create(championship=championship, iframe_url=iframe,
                              iframe_stats="cards for", date_updated=today)

    for championship, iframe in iframes[1].items():
        Iframe.objects.create(championship=championship, iframe_url=iframe,
                              iframe_stats="cards against", date_updated=today)

    return HttpResponse("Iframes Updated")


############################################   UPDATE DATAS   ##########################################################
def update_datas(request):
    driver = open_browser()

    cards_against_iframes = Iframe.objects.filter(iframe_stats="cards against")
    cards_for_iframes = Iframe.objects.filter(iframe_stats="cards for")

    for card_for_iframe in cards_for_iframes:
        get_data(url=card_for_iframe.iframe_url, championship=card_for_iframe.championship,
                 driver=driver, data_stats="cards for")

    for card_against_iframe in cards_against_iframes:
        get_data(url=card_against_iframe.iframe_url, championship=card_against_iframe.championship,
                 driver=driver, data_stats="cards against")
    return HttpResponse("Datas Update")
