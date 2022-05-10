from selenium.webdriver.common.by import By
from utils.constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP
from utils.selenium_functions import open_browser

iframes_yc_for = {}
iframes_yc_against = {}


def get_all_cards_iframes():
    """
    Return a tuple who contain two dictionary of cards iframes
    :return: (dict, dict)
    """
    driver = open_browser()
    for key, value in LEAGUES_URLS.items():
        card_link = value + CARDS
        get_card_iframe(link=card_link, championship=key, driver=driver)
    return iframes_yc_for, iframes_yc_against


def get_card_iframe(link, championship, driver):
    """
    Get a single iframe and save it in a local variable
    :param link: str
    :param championship: str
    :param driver: WebDriver
    :return: None
    """
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
