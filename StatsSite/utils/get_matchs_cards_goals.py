from selenium.webdriver.common.by import By
from blog.models import MatchsAVenir, MatchsTermine
from utils.get_matchs import open_browser


def get_matchs_cards_goals(match, date, url):
    driver = open_browser()
    driver.get(url)

    nb_goals = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement1"))
    nb_yellow_cards = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement4"))
    nb_red_cards = len(driver.find_elements(By.CSS_SELECTOR, "span.ico_evenement3"))

    new_query = MatchsAVenir.objects.filter(date=date, match=match.replace("|", " - "))

    if len(new_query) != 0:
        new_query_values = new_query.values()
        MatchsTermine.objects.create(match=new_query_values[0]['match'],
                                      championship=new_query_values[0]['championship'],
                                      date=new_query_values[0]['date'],
                                      slug=new_query_values[0]['slug'],
                                      home_team=new_query_values[0]['home_team'],
                                      away_team=new_query_values[0]['away_team'],
                                      nb_yellow_cards=nb_yellow_cards,
                                      nb_red_cards=nb_red_cards,
                                      nb_goals=nb_goals)
        MatchsAVenir.objects.filter(date=date, match=match.replace("|", " - ")).delete()