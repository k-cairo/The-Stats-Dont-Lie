import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP

iframes_yc_for = {}
iframes_yc_against = {}
iframes_corner_for = {}
iframes_corner_against = {}

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def get_card_iframe(link, championship):
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


def get_corner_iframe(link, championship):
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


def write_in_json_file(stats):
    if not os.path.exists("./iframes"):
        os.mkdir("./iframes")

    if not os.path.exists(f"./iframes/{stats}"):
        os.mkdir(f"./iframes/{stats}")

    if stats == "cards":
        json_object_1 = json.dumps(iframes_yc_for, indent=4)
        with open(f"./iframes/{stats}/iframes_{stats}_for.json", "w") as f:
            f.write(json_object_1)

        json_object_2 = json.dumps(iframes_yc_against, indent=4)
        with open(f"./iframes/{stats}/iframes_{stats}_against.json", "w") as f:
            f.write(json_object_2)

    elif stats == "corners":
        print(iframes_corner_for)
        print(iframes_corner_against)
        json_object_3 = json.dumps(iframes_corner_for, indent=4)
        with open(f"./iframes/{stats}/iframes_{stats}_for.json", "w") as f:
            f.write(json_object_3)

        json_object_4 = json.dumps(iframes_corner_against, indent=4)
        with open(f"./iframes/{stats}/iframes_{stats}_against.json", "w") as f:
            f.write(json_object_4)


def get_all_cards_iframes():
    for key, value in LEAGUES_URLS.items():
        card_link = value + CARDS
        get_card_iframe(link=card_link, championship=key)
    write_in_json_file(stats="cards")


def get_all_corners_iframes():
    for key, value in LEAGUES_URLS.items():
        corner_link = value + CORNERS
        get_corner_iframe(link=corner_link, championship=key)
    write_in_json_file(stats="corners")


