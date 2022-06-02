from selenium.webdriver.common.by import By
from blog.models import Data
from utils.get_matchs import today


def get_data(url, championship, driver, data_stats):
    teams = get_teams(driver=driver, url=url)
    cards_stats = get_cards_stats(driver=driver)
    update_database(championship=championship, home_teams=teams[0], home_stats=cards_stats[0],
                    away_teams=teams[1], away_stats=cards_stats[1], data_stats=data_stats)


def get_cards_stats(driver):
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
        Data.objects.create(championship=championship, datas=result, datas_stats=data_stats, date_updated=today)
    else:
        Data.objects.filter(championship=championship).update(datas=result, date_updated=today)
