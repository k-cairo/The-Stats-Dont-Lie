from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, date, timedelta
import locale
import os
from constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP

locale.setlocale(locale.LC_TIME, "fr_FR")


def open_browser():
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except:
        service = Service(executable_path="./chromedriver/chromedriver.exe")
    finally:
        driver = webdriver.Chrome(service=service)
    return driver


def test():
    driver = open_browser()
    driver.get("https://www.matchendirect.fr/foot-score/3724071-paris-saint-germain-nice.html")

    ht_href = driver.find_element(By.XPATH, '//*[@id="ajax-match-detail-1"]/div/div[3]/div[1]/a').get_attribute('href')
    at_href = driver.find_element(By.XPATH, '//*[@id="ajax-match-detail-1"]/div/div[3]/div[3]/a').get_attribute('href')

    get_historique_team_href(url=ht_href)


def get_historique_team_href(url):
    all_matchs_link = {}
    driver = open_browser()
    driver.get(url)

    # Accept Cookies function

    div_competitions = driver.find_elements(By.CSS_SELECTOR, "div.panel-info")

    for div_competition in div_competitions:
        try:
            competition = div_competition.find_element(By.CSS_SELECTOR, 'a').text
        except NoSuchElementException:
            pass
        else:
            all_matchs_link[competition] = []
            if not competition == "":
                div_matchs = div_competition.find_elements(By.CSS_SELECTOR, "tbody tr")
                for div_match in div_matchs:
                    try:
                        home_team = div_match.find_element(By.CSS_SELECTOR, "span.lm3_eq1").text.strip("*")
                        away_team = div_match.find_element(By.CSS_SELECTOR, "span.lm3_eq2").text.strip("*")
                        href_match = div_match.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                    except NoSuchElementException:
                        pass
                    else:
                        all_matchs_link[competition].append((home_team, away_team, href_match))

    for competition, list_matchs_link in all_matchs_link.items():
        if not competition == "":
            for match_link in list_matchs_link:
                print(f"{competition} : {match_link[0]} - {match_link[1]} | {match_link[2]}")
                get_matchs_cards_goals(url=match_link[2])


def get_matchs_cards_goals(url):
    driver = open_browser()
    driver.get(url)

    # Accept Cookies function

    match_date = driver.find_element(By.XPATH, '//*[@id="ajax-match-detail-1"]/div/div[1]/div/div/a[1]').text

    datetime_object = datetime.strptime(match_date, '%A %d %B %Y')
    date_format = datetime_object.strftime("%d-%m-%Y")

    if date_format < datetime.today().strftime("%d-%m-%Y"):
        goals = driver.find_elements(By.CSS_SELECTOR, "span.score")
        ht_goals = goals[0].text
        at_goals = goals[1].text

        nb_goals = int(ht_goals) + int(at_goals)
        match_date = driver.find_element(By.XPATH, '//*[@id="ajax-match-detail-1"]/div/div[1]/div/div/a[1]').text
        nb_yellow_cards = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement4"))
        nb_red_cards = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement3"))

        print(f"Match Date: {match_date}")
        print(f"Yellow Cards: {nb_yellow_cards}")
        print(f"Goals: {nb_goals}")
        print(f"Yellow Cards: {nb_yellow_cards}")
        print(f"Red Cards: {nb_red_cards}")
        print()
        print()


def get_double_chance_predictions(day, ht, at):
    if day == datetime.today().strftime("%d-%m-%Y"):
        url = "https://www.mybets.today/soccer-predictions/double-chance-predictions/"
    elif day ==(date.today() + timedelta(days=1)).strftime("%d-%m-%Y"):
        url = "https://www.mybets.today/soccer-predictions/double-chance-predictions/tomorrow/"
    else:
        url = "https://www.mybets.today/soccer-predictions/double-chance-predictions/after-tomorrow/"

    driver = open_browser()
    driver.get(url)

    divs_match = driver.find_elements(By.CSS_SELECTOR, "a.linkgames")

    for div_match in divs_match:
        home_team = div_match.find_element(By.CSS_SELECTOR, 'span.homespan').text
        away_team = div_match.find_element(By.CSS_SELECTOR, 'span.awayspan').text
        if home_team.lower() == ht.lower or away_team.lower() == at.lower():
            double_chance_prediction = div_match.find_element(By.CSS_SELECTOR, 'div.tipdiv').text
            return double_chance_prediction


day_list = [1, 2, 3, 4, 5]

print(day_list[:-2])



