import manager as manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

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
    "taly - Serie A": "https://www.thestatsdontlie.com/football/europe/italy/serie-a",
    "Poland - Ekstraklasa": "https://www.thestatsdontlie.com/football/europe/poland/ekstraklasa",
    "Portugal - Primeira Liga": "https://www.thestatsdontlie.com/football/europe/portugal/primeira-liga",
    "Scotland - Premiership": "https://www.thestatsdontlie.com/football/uk-ireland/scotland/premiership",
    "Spain - La Liga": "https://www.thestatsdontlie.com/football/europe/spain/la-liga",
    "Spain - Segunda Division": "https://www.thestatsdontlie.com/football/europe/spain/segunda-division",
    "Sweden - Allsvenskan": "https://www.thestatsdontlie.com/football/europe/sweden/allsvenskan",
    "Turkey - Super Lig": "https://www.thestatsdontlie.com/football/europe/turkey/super-lig",
    "USA - MLS": "https://www.thestatsdontlie.com/football/n-s-america/usa/mls"
}

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://www.google.com")

