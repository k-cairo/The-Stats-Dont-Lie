import manager as manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

CARDS = "/cards"
CORNERS = "/corners"
LEAGUES_URLS = {
    "Australia - A-League": "https://www.thestatsdontlie.com/football/rest-of-the-world/australia/a-league",
    "Austria - Bundesliga": "https://www.thestatsdontlie.com/football/europe/austria/bundesliga",
    "Belgium - Pro League": "https://www.thestatsdontlie.com/football/europe/belgium/pro-league",
    "Brazil - Serie A": "https://www.thestatsdontlie.com/football/n-s-america/brazil/serie-a",
    "China - Super League": "https://www.thestatsdontlie.com/football/rest-of-the-world/china/super-league",
    "Croatia - 1. HNL": "https://www.thestatsdontlie.com/football/europe/croatia/1-hnl",
    "Czech Republic - 1. Liga": "https://www.thestatsdontlie.com/football/europe/czech-republic/1-liga",
    "Denmark - Superliga": "https://www.thestatsdontlie.com/football/europe/denmark/superliga",
    "England - Premier League": "https://www.thestatsdontlie.com/football/uk-ireland/england/premier-league",
    "England - Championship": "https://www.thestatsdontlie.com/football/uk-ireland/england/championship",
    "Finland - Veikkausliiga": "https://www.thestatsdontlie.com/football/europe/finland/veikkausliiga",
    "France - Ligue 1": "https://www.thestatsdontlie.com/football/europe/france/ligue-1",
    "France - Ligue 2": "https://www.thestatsdontlie.com/football/europe/france/ligue-2",
    "Germany - Bundesliga": "https://www.thestatsdontlie.com/football/europe/germany/bundesliga",
    "Germany - 2. Bundesliga": "https://www.thestatsdontlie.com/football/europe/germany/2-bundesliga",
    "Holland - Eredivisie": "https://www.thestatsdontlie.com/football/europe/holland/eredivisie",
    "Holland - Eerste Divisie": "https://www.thestatsdontlie.com/football/europe/holland/eerste-divisie",
    "Italy - Serie A": "https://www.thestatsdontlie.com/football/europe/italy/serie-a",
    "Poland - Ekstraklasa": "https://www.thestatsdontlie.com/football/europe/poland/ekstraklasa",
    "Portugal - Primeira Liga": "https://www.thestatsdontlie.com/football/europe/portugal/primeira-liga",
    "Scotland - Premiership": "https://www.thestatsdontlie.com/football/uk-ireland/scotland/premiership",
    "Spain - La Liga": "https://www.thestatsdontlie.com/football/europe/spain/la-liga",
    "Spain - Segunda Division": "https://www.thestatsdontlie.com/football/europe/spain/segunda-division",
    "Sweden - Allsvenskan": "https://www.thestatsdontlie.com/football/europe/sweden/allsvenskan",
    "Turkey - Super Lig": "https://www.thestatsdontlie.com/football/europe/turkey/super-lig",
    "USA - MLS": "https://www.thestatsdontlie.com/football/n-s-america/usa/mls"
}
TEAMS_IN_CHAMPIONSHIP = {
    "Australia - A-League": 12, "Austria - Bundesliga": 12, "Belgium - Pro League": 18, "Brazil - Serie A": 20,
    "China - Super League": 16, "Croatia - 1. HNL": 10, "Czech Republic - 1. Liga": 16, "Denmark - Superliga": 12,
    "England - Premier League": 20, "England - Championship": 24, "Finland - Veikkausliiga": 12, "France - Ligue 1": 20,
    "France - Ligue 2": 20, "Germany - Bundesliga": 18, "Germany - 2. Bundesliga": 18, "Holland - Eredivisie": 18,
    "Holland - Eerste Divisie": 20, "Italy - Serie A": 20, "Poland - Ekstraklasa": 18, "Portugal - Primeira Liga": 18,
    "Scotland - Premiership": 12, "Spain - La Liga": 20, "Spain - Segunda Division": 22, "Sweden - Allsvenskan": 16,
    "Turkey - Super Lig": 20, "USA - MLS": 27}

all_iframes = {}

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def get_iframe(link, championship):
    driver.get(link)
    nb_team = TEAMS_IN_CHAMPIONSHIP[championship]
    try:
        iframe = driver.find_element(By.CSS_SELECTOR, f"div.embed-container{nb_team} iframe").get_attribute('src')
    except:
        print(f"Erreur avec le championnat : {championship}")
    else:
        content = f"{championship} - {iframe}"
        with open("./iframes.txt", 'a') as iframe_file:
            iframe_file.write(f"{content}\n")


def get_data():
    other_teams = []
    home_teams = []
    driver.get("https://docs.google.com/spreadsheets/d/1kYzcpxZo90jHOhKz3rCKZtLUtmMcDnv_qKmtRoK_d9I/pubhtml?gid=1157183632&single=true&widget=false&headers=false&chrome=false")

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

    print(f"Home Teams : {home_teams}")
    print(f"Home Stats : {home_stats}")
    print(f"Away Teams : {away_teams}")
    print(f"Away Stats : {away_stats}")

    return home_stats, home_teams, away_stats, away_teams










if __name__ == "__main__":
    # for key, value in LEAGUES_URLS.items():
    #     card_link = value + CARDS
    #     get_iframe(link=card_link, championship=key)
    get_data()


