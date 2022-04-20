import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta, date
from webdriver_manager.chrome import ChromeDriverManager
from constant import LIST_CHAMPIONSHIP, CONVERSION_LIST
import os

all_matchs = {}


def get_user_date():
    tomorrow = date.today() + timedelta(days=1)
    tomorrow_format = tomorrow.strftime("%d-%m-%Y")
    today = datetime.today().strftime("%d-%m-%Y")

    user_date = input("Vous voulez la liste de matchs pour quel jour?(au format JJ-MM-AAAA ou Aujourd'hui et Demain): ")

    if user_date.lower() == "aujourd'hui":
        user_date = today
    elif user_date.lower() == "demain":
        user_date = tomorrow_format

    url = f"https://www.matchendirect.fr/resultat-foot-{user_date}/"
    get_all_matchs(url=url, date=user_date)


def get_all_matchs(url, date):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    all_div_championships = driver.find_elements(By.CSS_SELECTOR, "div div.panel.panel-info")

    for div_championship in all_div_championships[:-2]:
        try:
            championship = div_championship.find_element(By.CSS_SELECTOR, "h3.panel-title a").text
        except NoSuchElementException:
            print("Problème avec un Championnat")
        else:
            if championship in LIST_CHAMPIONSHIP:
                championship_format = format_championships_names(championship=championship)
                all_matchs[championship_format] = []
                raw_matchs = div_championship.find_elements(By.CSS_SELECTOR, "tbody td.lm3")
                for row_match in raw_matchs:
                    home_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq1").text
                    home_team_format = format_teams_names(team=home_team)
                    away_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq2").text
                    away_team_format = format_teams_names(team=away_team)
                    format_match = f"{home_team_format}-{away_team_format}"
                    all_matchs[championship_format].append(format_match)

    write_to_json_file(content=all_matchs, date2=date)


def write_to_json_file(content, date2):
    if not os.path.exists("./Liste de Matchs"):
        os.mkdir("./Liste de Matchs")

    json_object = json.dumps(content, indent=4)
    with open(f"./liste de Matchs/{date2}.json", "w") as f:
        f.write(json_object)


def format_teams_names(team):
    return team.replace("Paris Saint-Germain", "PSG").replace("Manchester City", "Man City")\
        .replace("Espanyol Barcelone", "Espanyol").replace("Séville", "Sevilla").replace("Cadix", "Cadiz")\
        .replace("Athletic Bilbao", 'Ath. Bilbao').replace("Barcelone", "Barcelona").replace("Värnamo", "Varnamo")\
        .replace("Malmö FF", "Malmo FF").replace("St Étienne", "St. Etienne").replace("Grenade", "Granada")\
        .replace("Atlético Madrid", "Atl. Madrid").replace('Western Sydney Wanderers', "WS Wanderers")\
        .replace("Dinamo Zagreb", "Din. Zagreb").replace("KKS Lech Poznan", "Lech")\
        .replace("GKS Górnik Leczna SA", "Leczna").replace("MKS Pogon Szczecin", "Pogon Szczecin")\
        .replace("Raków Czestochowa", "Rakow").replace("Bohemians 1905", "Bohemians")\
        .replace("Hradec Králové", "Hradec Kralove").replace("Mladá Boleslav", "Mlada Boleslav")\
        .replace("Viktoria Plzeň", "Plzen").replace("České Budějovice", "Ceske Budejovice")\
        .replace("Karviná", "Karvina").replace("FK Pardubice", "Pardubice").replace("Zlín", "Zlin")\
        .replace("Baník Ostrava", "Ostrava").replace("Slovácko", "Slovacko").replace("Slovan Liberec", "Liberec")\
        .replace("AIK", "AIK Stockholm").replace("Varberg", "Varbergs").replace("IFK Göteborg", "Goteborg")\
        .replace("Djurgården", "Djurgarden").replace("Norrköping", "Norrkoping").replace("Häcken", "Hacken")\
        .replace("Mjällby", "Mjallby").replace("GIF Sundsvall", "Sundsvall").replace("Amiens SC", "Amiens")\
        .replace("Quevilly", "Quevilly Rouen").replace("Nîmes", "Nimes").replace("Pau", "Pau FC")\
        .replace("Ajaccio", "AC Ajaccio").replace("Wolfsbourg", "Wolfsburg").replace("Mayence", "Mainz")\
        .replace("Huddersfield Town", "Huddersfield").replace("Fortuna Düsseldorf", "Dusseldorf")\
        .replace("Dynamo Dresde", "Dresden").replace("Karlsruhe", "Karlsruher").replace("Caykur Rizespor", "Rizespor")\
        .replace("Volendam", "FC Volendam").replace("Roda JC", "Roda").replace("AZ II", "Jong AZ")


def format_championships_names(championship):
    return CONVERSION_LIST[championship]


if __name__ == "__main__":
    get_user_date()