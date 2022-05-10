import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

YELLOW_CARD_FOR_PATH = "./iframes/cards/iframes_cards_for.json"
YELLOW_CARD_AGAINST_PATH = "./iframes/cards/iframes_cards_against.json"
FULL_TIME_CORNER_FOR = "./iframes/corners/iframes_corners_for.json"
FULL_TIME_CORNER_AGAINST = "./iframes/corners/iframes_corners_against.json"

ALL_PATHS = [YELLOW_CARD_AGAINST_PATH, YELLOW_CARD_FOR_PATH, FULL_TIME_CORNER_AGAINST, FULL_TIME_CORNER_FOR]


def open_browser():
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except:
        service = Service(executable_path="./chromedriver/chromedriver.exe")
    finally:
        driver = webdriver.Chrome(service=service)
    return driver


def get_all_datas():
    driver = open_browser()

    for path in ALL_PATHS:
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
                for championship, iframe in data.items():
                    get_data(url=iframe, championship=championship, path_iframe=path, driver=driver)


def get_data(url, championship, path_iframe, driver):
    other_teams = []
    home_teams = []
    driver.get(url)

    # Get Home team and Away team
    teams = driver.find_elements(By.CSS_SELECTOR, "tbody tr td a")
    for i, team in enumerate(teams):
        if i % 3 == 0:
            home_teams.append(team.text)
        else:
            other_teams.append(team.text)
    away_teams = [team for i, team in enumerate(other_teams) if i % 2 == 0]

    # Get Average Stats
    home_stats = []
    away_stats = []
    all_tr = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
    for tr in all_tr[2:-1]:
        all_td = tr.find_elements(By.CSS_SELECTOR, "td")
        home_stat = all_td[4].text
        away_stat = all_td[9].text
        home_stats.append(home_stat)
        away_stats.append(away_stat)

    write_data_in_json_file(championship=championship, home_teams=home_teams, home_stats=home_stats,
                            away_teams=away_teams, away_stats=away_stats, path_iframe=path_iframe)


def write_data_in_json_file(championship, home_teams, home_stats, away_teams, away_stats, path_iframe):
    outfile_list = ["cards_for", "cards_against", "corners_for", "corners_against"]
    outfile = ""

    for file in outfile_list:
        if file in path_iframe:
            outfile = file

    if not os.path.exists("./data"):
        os.mkdir("./data")

    if not os.path.exists(f"./data/{championship}"):
        os.mkdir(f"./data/{championship}")

    result = {
        "Home Teams": [],
        "Away Teams": []
    }

    for i, team in enumerate(home_teams):
        result["Home Teams"].append({team: home_stats[i]})

    for i, team in enumerate(away_teams):
        result["Away Teams"].append({team: away_stats[i]})

    json_object = json.dumps(result, indent=4)
    with open(f"./data/{championship}/{championship}_{outfile}.json", "w") as f:
        f.write(json_object)


if __name__ == "__main__":

    get_all_datas()