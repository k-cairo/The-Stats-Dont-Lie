from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from utils.constant import today
from utils.selenium_functions import open_browser
from blog.models import Iframe, Data


def get_data(url, championship, driver, data_stats):
    teams = get_teams(driver=driver, url=url)
    stats = get_stats(driver=driver)
    update_database(championship=championship, home_teams=teams[0], home_stats=stats[0],
                    away_teams=teams[1], away_stats=stats[1], data_stats=data_stats)


def get_teams(driver, url):
    other_teams = []
    home_teams = []
    driver.get(url)

    teams = driver.find_elements(By.CSS_SELECTOR, "tbody tr td a")
    for i, team in enumerate(teams):
        if i % 3 == 0:
            home_teams.append(team.text)
        else:
            other_teams.append(team.text)
    away_teams = [team for i, team in enumerate(other_teams) if i % 2 == 0]
    return home_teams, away_teams


def get_stats(driver):
    home_stats = []
    away_stats = []
    all_tr = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
    for tr in all_tr[2:-1]:
        all_td = tr.find_elements(By.CSS_SELECTOR, "td")
        home_stat = all_td[4].text
        away_stat = all_td[9].text
        home_stats.append(home_stat)
        away_stats.append(away_stat)
    return home_stats, away_stats


def update_database(championship, home_teams, home_stats, away_teams, away_stats, data_stats):
    result = {
        "Home Teams": [],
        "Away Teams": []
    }

    for i, team in enumerate(home_teams):
        result["Home Teams"].append({team: home_stats[i]})

    for i, team in enumerate(away_teams):
        result["Away Teams"].append({team: away_stats[i]})

    if len(Data.objects.filter(championship=championship).filter(datas_stats=data_stats)) == 0:
        return Data.objects.create(championship=championship, datas=result, datas_stats=data_stats, date_updated=today)
    else:
        return Data.objects.filter(championship=championship).filter(datas_stats=data_stats).update(
            datas=result, date_updated=today)


class Command(BaseCommand):
    help = 'Update cards and corners Datas'

    def handle(self, *args, **options):
        driver = open_browser()

        # GET ALL STATS IFRAMES
        cards_against_iframes = Iframe.objects.filter(iframe_stats="cards against")
        cards_for_iframes = Iframe.objects.filter(iframe_stats="cards for")
        corners_against_iframes = Iframe.objects.filter(iframe_stats="corners against")
        corners_for_iframes = Iframe.objects.filter(iframe_stats="corners for")

        # UPDATE CARDS FOR DATAS
        for card_for_iframe in cards_for_iframes:
            get_data(url=card_for_iframe.iframe_url, championship=card_for_iframe.championship,
                     driver=driver, data_stats="cards for")

        # UPDATE CARDS AGAINST DATAS
        for card_against_iframe in cards_against_iframes:
            get_data(url=card_against_iframe.iframe_url, championship=card_against_iframe.championship,
                     driver=driver, data_stats="cards against")

        # UPDATE CORNERS FOR DATAS
        for corner_for_iframe in corners_for_iframes:
            get_data(url=corner_for_iframe.iframe_url, championship=corner_for_iframe.championship,
                     driver=driver, data_stats="corners for")

        # UPDATE CORNERS AGAINST DATAS
        for corner_against_iframe in corners_against_iframes:
            get_data(url=corner_against_iframe.iframe_url, championship=corner_against_iframe.championship,
                     driver=driver, data_stats="corners against")

        self.stdout.write('Cards and Corners Datas Updated Successfully')
