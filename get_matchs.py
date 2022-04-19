import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from constant import LIST_CHAMPIONSHIP
import os

##### SITE POUR RECHERCHER LES MATCHS #####
URL = "https://www.matchendirect.fr/live-foot/"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(URL)

today = datetime.today().strftime("%A %d %B %Y")
all_matchs = {}


def get_all_matchs():
    all_div_championships = driver.find_elements(By.CSS_SELECTOR, "div div.panel.panel-info")

    for div_championship in all_div_championships:
        try:
            championship = div_championship.find_element(By.CSS_SELECTOR, "h3.panel-title a").text
        except NoSuchElementException:
            print("Problème avec un Championnat")
        else:
            if championship in LIST_CHAMPIONSHIP:
                print(championship)
                all_matchs[championship] = []
                raw_matchs = div_championship.find_elements(By.CSS_SELECTOR, "tbody td.lm3")
                for row_match in raw_matchs:
                    home_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq1").text
                    away_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq2").text
                    format_match = f"{home_team}-{away_team}"
                    all_matchs[championship].append(format_match)

    write_to_json_file(content=all_matchs)


def write_to_json_file(content):
    if not os.path.exists("./Liste de Matchs"):
        os.mkdir("./Liste de Matchs")

    json_object = json.dumps(content, indent=4)
    with open(f"./Liste de Matchs/{today}.json", "w") as f:
        f.write(json_object)