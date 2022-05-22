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

            championship = target_match.championship
            home_team = target_match.home_team
            away_team = target_match.away_team

            home_team_histo = MatchsTermine.objects.filter(target_team=home_team)
            away_team_histo = MatchsTermine.objects.filter(target_team=away_team)

            cards_for_data = Data.objects.filter(championship=championship).filter(datas_stats="cards for").get().datas
            cards_against_data = Data.objects.filter(championship=championship).filter(datas_stats="cards against").get().datas

            home_team_cards_for_average = 0
            away_team_cards_for_average = 0
            home_team_cards_against_average = 0
            away_team_cards_against_average = 0

            for data1 in cards_for_data["Home Teams"]:
                for team1, average_card1 in data1.items():
                    if team1 == home_team:
                        home_team_cards_for_average = average_card1
                        print(home_team_cards_for_average)

            for data2 in cards_for_data["Away Teams"]:
                for team2, average_card2 in data2.items():
                    if team2 == away_team:
                        away_team_cards_for_average = average_card2

            for data3 in cards_against_data["Home Teams"]:
                for team3, average_card3 in data3.items():
                    if team3 == home_team:
                        home_team_cards_against_average = average_card3
                        print(home_team_cards_against_average)

            for data4 in cards_against_data["Away Teams"]:
                for team4, average_card4 in data4.items():
                    if team4 == away_team:
                        away_team_cards_against_average = average_card4

    return render(request, "blog/match_details.html", context={"home_team_histo": home_team_histo,
                                                               "away_team_histo": away_team_histo,
                                                               "home_team": home_team,
                                                               "away_team": away_team,
                                                               "target_match": target_match,
                                                               "home_team_cards_for_average": home_team_cards_for_average,
                                                               "away_team_cards_for_average": away_team_cards_for_average,
                                                               "home_team_cards_against_average": home_team_cards_against_average,
                                                               "away_team_cards_against_average": away_team_cards_against_average})


########################################   UPDATE MATCHS A VENIR   #####################################################
def update_matchs_a_venir(request):
<<<<<<< HEAD
    # # Update Iframes
    # get_all_cards_iframes()
    #
    # # Update Datas
    # driver = open_browser()
    #
    # cards_against_iframes = Iframe.objects.filter(iframe_stats="cards against")
    # cards_for_iframes = Iframe.objects.filter(iframe_stats="cards for")
    #
    # for card_for_iframe in cards_for_iframes:
    #     get_data(url=card_for_iframe.iframe_url, championship=card_for_iframe.championship,
    #              driver=driver, data_stats="cards for")
    #
    # for card_against_iframe in cards_against_iframes:
    #     get_data(url=card_against_iframe.iframe_url, championship=card_against_iframe.championship,
    #              driver=driver, data_stats="cards against")
=======
    # Update Iframes
    # get_all_cards_iframes()

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
>>>>>>> 78ec3404ca4350bc3e2fdf1449485cea63e0e104

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
    all_teams_query = TeamIframe.objects.all()

    for query in all_teams_query:
        driver = open_browser()
        driver.get(url=query.iframe_url)

        trs = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

        for tr in trs[3:-2]:
            tds = tr.find_elements(By.CSS_SELECTOR, "td")
            date = tds[1].text
            ht = tds[2].text
            ht_score = tds[3].text
            at_score = tds[4].text
            at = tds[5].text
            corner_for = tds[13].text
            corner_against = tds[14].text
            yellow_card_for = tds[16].text
            yellow_card_against = tds[17].text
            red_card_for = tds[18].text
            red_card_against = tds[19].text
            datas = (date, ht, ht_score, at_score, at, corner_for, corner_against, yellow_card_for, yellow_card_against,
                     red_card_for, red_card_against)

            if len(MatchsTermine.objects.filter(target_team=query.team).filter(date=date)) == 0 and all(
                    data != "" for data in datas):
                MatchsTermine.objects.create(target_team=query.team,
                                             date=date,
                                             home_team=ht,
                                             score=f"{ht_score} - {at_score}",
                                             away_team=at,
                                             corner_for=corner_for,
                                             corner_against=corner_against,
                                             yellow_card_for=yellow_card_for,
                                             yellow_card_against=yellow_card_against,
                                             red_card_for=red_card_for,
                                             red_card_against=red_card_against)
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
                                '/html/body/div[1]/div[2]/main/div/section/div/div/div[5]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys(
                "cairo.kevin72@gmail.com")
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
