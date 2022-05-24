from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from utils.constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP, today
from utils.selenium_functions import open_browser
from blog.models import Iframe

iframes_yc_for = {}
iframes_yc_against = {}
iframes_corner_for = {}
iframes_corner_against = {}


def get_card_iframe(link, championship, driver):
    driver.get(link)
    nb_team = TEAMS_IN_CHAMPIONSHIP[championship]
    try:
        iframes = driver.find_elements(By.CSS_SELECTOR, f"div.embed-container{nb_team} iframe")
        iframe_yc_for = iframes[0].get_attribute('src')
        iframe_yc_against = iframes[1].get_attribute('src')
    except IndexError:
        print(f"Erreur avec le championnat : {championship} - CARDS")
    else:
        iframes_yc_for[championship] = iframe_yc_for
        iframes_yc_against[championship] = iframe_yc_against


def get_corner_iframe(link, championship, driver):
    driver.get(link)
    nb_team = TEAMS_IN_CHAMPIONSHIP[championship]
    try:
        iframes = driver.find_elements(By.CSS_SELECTOR, f"div.embed-container{nb_team} iframe")
        iframe_corner_for = iframes[0].get_attribute('src')
        iframe_corner_against = iframes[1].get_attribute('src')
    except IndexError:
        print(f"Erreur avec le championnat : {championship} - CORNERS")
    else:
        iframes_corner_for[championship] = iframe_corner_for
        iframes_corner_against[championship] = iframe_corner_against


def update_cards_iframes():
    for championship, iframe in iframes_yc_for.items():
        if Iframe.objects.filter(championship=championship).filter(iframe_stats="cards for") == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="cards for", date_updated=today)
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="cards for").update(iframe_url=iframe,
                                                                                                     date_updated=today)

    for championship, iframe in iframes_yc_against.items():
        if Iframe.objects.filter(championship=championship).filter(iframe_stats="cards against") == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="cards against", date_updated=today)
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="cards against").update(
                iframe_url=iframe, date_updated=today)


def update_corners_iframes():
    for championship, iframe in iframes_corner_for.items():
        if Iframe.objects.filter(championship=championship).filter(iframe_stats="corners for") == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="corners for", date_updated=today)
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="corners for").update(
                iframe_url=iframe, date_updated=today)

    for championship, iframe in iframes_corner_against.items():
        if Iframe.objects.filter(championship=championship).filter(iframe_stats="corners against") == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="corners against", date_updated=today)
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="corners against").update(
                iframe_url=iframe, date_updated=today)


class Command(BaseCommand):
    help = "Get Cards and Corners Iframes from source. Save it in database if doesn't exist else update it in database"

    def handle(self, *args, **options):
        driver = open_browser()

        # GET CARDS IFRAMES
        for key, value in LEAGUES_URLS.items():
            card_link = value + CARDS
            get_card_iframe(link=card_link, championship=key, driver=driver)
        update_cards_iframes()
        iframes_yc_for.clear()
        iframes_yc_against.clear()

        # GET CORNERS IFRAMES
        for key, value in LEAGUES_URLS.items():
            corner_link = value + CORNERS
            get_corner_iframe(link=corner_link, championship=key, driver=driver)
        update_corners_iframes()
        iframes_corner_for.clear()
        iframes_corner_against.clear()

        self.stdout.write('Cards and Corners Iframes Updated Successfully')
