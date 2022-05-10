from selenium.webdriver.common.by import By
from utils.constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP
from utils.selenium_functions import open_browser

iframes_corner_for = {}
iframes_corner_against = {}


def get_all_corners_iframes():
    """
    Return a tuple who contain two dictionary of corners iframes
    :return: (dict, dict)
    """
    driver = open_browser()
    for key, value in LEAGUES_URLS.items():
        corner_link = value + CORNERS
        get_corner_iframe(link=corner_link, championship=key, driver=driver)
    return iframes_corner_for, iframes_corner_against


def get_corner_iframe(link, championship, driver):
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
        iframe_corner_for = iframes[5].get_attribute('src')
        iframe_corner_against = iframes[6].get_attribute('src')
    except IndexError:
        print(f"Erreur avec le championnat : {championship} - CORNERS")
    else:
        iframes_corner_for[championship] = iframe_corner_for
        iframes_corner_against[championship] = iframe_corner_against
