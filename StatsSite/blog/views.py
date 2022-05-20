import time
from selenium.webdriver.common.keys import Keys
from django.shortcuts import render, HttpResponse
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from utils.constant import LOGO_LIST, LIST_CHAMPIONSHIP
from utils.get_data import get_data
from utils.get_matchs import format_championships_names, format_teams_names, day_list, today, tomorrow, j2, \
    get_all_matchs, get_matchs_cards_goals, get_double_chance_predictions, define_card_bet, get_cards_queryset, \
    get_home_away_team_cards_stats, calculate_total_cards
from utils.selenium_functions import open_browser, accept_cookie
from utils.get_cards_iframes import get_all_cards_iframes
from .models import MatchsAVenir, Data, Iframe, MatchsTermine, TeamIframe
from django.db.models import Q
from slugify import slugify
from utils.constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP

BASE_DIRECTORY = Path(__file__).resolve().parent.parent.parent


################################################   INDEX   #############################################################
def index(request):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    context = {"matchs": today_j3_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


##################################   TODAY, TOMORROW, J2 MATCHS PAGES   ################################################
def today_matchs(request):
    today_matchs = MatchsAVenir.objects.filter(date=today)
    context = {"matchs": today_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def tomorrow_matchs(request):
    tomorrow_matchs = MatchsAVenir.objects.filter(date=tomorrow)
    context = {"matchs": tomorrow_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def j2_matchs(request):
    j2_matchs = MatchsAVenir.objects.filter(date=j2)
    context = {"matchs": j2_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


############################################   MATCH DETAILS   #########################################################
# TODO
def match_details(request, slug):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    for match in today_j3_matchs:
        if match.slug == slug:
            target_match = match
            print(f"Home Team : {match.home_team}")
            print(f"Away Team : {match.away_team}")

    home_team_queryset = TeamIframe.objects.filter(team=match.home_team)
    away_team_queryset = TeamIframe.objects.filter(team=match.away_team)

    home_team_iframe = home_team_queryset.values()[0]["iframe_url"]
    away_team_iframe = away_team_queryset.values()[0]["iframe_url"]

    
    return render(request, "blog/match_details.html")


########################################   UPDATE MATCHS A VENIR   #####################################################
def update_matchs_a_venir(request):
    # Update Iframes
    get_all_cards_iframes()

    # Update Datas
    driver = open_browser()

    cards_against_iframes = Iframe.objects.filter(iframe_stats="cards against")
    cards_for_iframes = Iframe.objects.filter(iframe_stats="cards for")

    for card_for_iframe in cards_for_iframes:
        get_data(url=card_for_iframe.iframe_url, championship=card_for_iframe.championship,
                 driver=driver, data_stats="cards for")

    for card_against_iframe in cards_against_iframes:
        get_data(url=card_against_iframe.iframe_url, championship=card_against_iframe.championship,
                 driver=driver, data_stats="cards against")

    # Check if day already in database (Next 3 days)
    for day in day_list:
        data_dates = MatchsAVenir.objects.filter(date=day)
        if len(data_dates) == 0:
            all_matchs = get_all_matchs(day)

            for championship, rencontres in all_matchs.items():
                for rencontre in rencontres:
                    if not MatchsAVenir.objects.filter(match=rencontre.replace('|', ' - '), date=day).exists():
                        teams = rencontre.split("|")
                        home_team = teams[0]
                        away_team = teams[1]

                        cards_querysets = get_cards_queryset(championship=championship)

                        all_teams_cards_stats = get_home_away_team_cards_stats(cards_querysets, home_team, away_team)

                        total_cards = calculate_total_cards(home_team_cards_for_average=all_teams_cards_stats[0],
                                                            away_team_cards_for_average=all_teams_cards_stats[2],
                                                            home_team_cards_against_average=all_teams_cards_stats[1],
                                                            away_team_cards_against_average=all_teams_cards_stats[3])

                        card_bet = define_card_bet(total_cards=total_cards)

                        double_chance_predict = get_double_chance_predictions(day=day, ht=home_team, at=away_team)

                        MatchsAVenir.objects.create(match=rencontre.replace('|', ' - '),
                                                    championship=championship,
                                                    date=day,
                                                    slug=slugify(rencontre),
                                                    home_team=rencontre.split("|")[0],
                                                    away_team=rencontre.split("|")[1],
                                                    home_team_cards_for_average=all_teams_cards_stats[0],
                                                    home_team_cards_against_average=all_teams_cards_stats[1],
                                                    away_team_cards_for_average=all_teams_cards_stats[2],
                                                    away_team_cards_against_average=all_teams_cards_stats[3],
                                                    card_bet=card_bet,
                                                    double_chance_predict=double_chance_predict)
    return HttpResponse("Matchs A Venir list Updated")


########################################   UPDATE MATCHS TERMINES   ####################################################
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
                print(f"Problème avec un Championnat: {championship}")
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
    all_links = {}
    driver = open_browser()
    querysets = Iframe.objects.filter(iframe_stats="cards against")

    for queryset in querysets:
        driver.get(url=queryset.iframe_url)

        div_tbody = driver.find_element(By.CSS_SELECTOR, "tbody")
        all_tr = div_tbody.find_elements(By.CSS_SELECTOR, "tr")

        for tr in all_tr[2:-1]:
            try:
                team = tr.find_element(By.CSS_SELECTOR, "td a").text
            except NoSuchElementException:
                print("Problem")
            else:
                team_link = tr.find_element(By.CSS_SELECTOR, "td a").get_attribute("href")
                all_links[team] = team_link

    for team, link in all_links.items():
        driver.get(link)
        try:
            driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[2]/main/div/section/div/div/div[5]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys("cairo.kevin72@gmail.com")
            driver.find_element(By.XPATH, '//*[@id="user_pass"]').send_keys("31Mars1988" + Keys.ENTER)
        except NoSuchElementException:
            pass
        finally:
            divs_content = driver.find_elements(By.CSS_SELECTOR, "div.tab-content")
            iframe = divs_content[1].find_element(By.CSS_SELECTOR, "iframe").get_attribute("src")

            if len(TeamIframe.objects.filter(team=team)) == 0:
                TeamIframe.objects.create(team=team,
                                          iframe_url=iframe,
                                          iframe_stats="histo_overall",
                                          date_updated=today)
            else:
                TeamIframe.objects.filter(team=team).update(iframe_url=iframe, date_updated=today)

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
