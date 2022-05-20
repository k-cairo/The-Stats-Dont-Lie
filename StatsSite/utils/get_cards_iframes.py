from selenium.webdriver.common.by import By
from utils.constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP
from utils.selenium_functions import open_browser
from utils.get_matchs import today
from blog.models import Iframe

iframes_yc_for = {}
iframes_yc_against = {}


def get_all_cards_iframes():
    driver = open_browser()
    for key, value in LEAGUES_URLS.items():
        card_link = value + CARDS
        get_card_iframe(link=card_link, championship=key, driver=driver)
    update_cards_iframes()
    iframes_yc_for.clear()
    iframes_yc_against.clear()


def get_card_iframe(link, championship, driver):
    driver.get(link)
    nb_team = TEAMS_IN_CHAMPIONSHIP[championship]
    try:
        iframes = driver.find_elements(By.CSS_SELECTOR, f"div.embed-container{nb_team} iframe")
        iframe_yc_for = iframes[0].get_attribute('src')
        iframe_yc_against = iframes[1].get_attribute('src')
    except IndexError:
        print(f"Erreur avec le championnat : {championship} - CARTONS")
    else:
        iframes_yc_for[championship] = iframe_yc_for
        iframes_yc_against[championship] = iframe_yc_against


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
