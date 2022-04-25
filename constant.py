CARDS = "/cards"
CORNERS = "/corners"
LEAGUES_URLS = {
    "Australia": "https://www.thestatsdontlie.com/football/rest-of-the-world/australia/a-league",
    "Austria": "https://www.thestatsdontlie.com/football/europe/austria/bundesliga",
    "Belgium": "https://www.thestatsdontlie.com/football/europe/belgium/pro-league",
    "Brazil": "https://www.thestatsdontlie.com/football/n-s-america/brazil/serie-a",
    "China": "https://www.thestatsdontlie.com/football/rest-of-the-world/china/super-league",
    "Croatia": "https://www.thestatsdontlie.com/football/europe/croatia/1-hnl",
    "Czech_Republic": "https://www.thestatsdontlie.com/football/europe/czech-republic/1-liga",
    "Denmark": "https://www.thestatsdontlie.com/football/europe/denmark/superliga",
    "England1": "https://www.thestatsdontlie.com/football/uk-ireland/england/premier-league",
    "England2": "https://www.thestatsdontlie.com/football/uk-ireland/england/championship",
    "Finland": "https://www.thestatsdontlie.com/football/europe/finland/veikkausliiga",
    "France1": "https://www.thestatsdontlie.com/football/europe/france/ligue-1",
    "France2": "https://www.thestatsdontlie.com/football/europe/france/ligue-2",
    "Germany1": "https://www.thestatsdontlie.com/football/europe/germany/bundesliga",
    "Germany2": "https://www.thestatsdontlie.com/football/europe/germany/2-bundesliga",
    "Holland1": "https://www.thestatsdontlie.com/football/europe/holland/eredivisie",
    "Holland2": "https://www.thestatsdontlie.com/football/europe/holland/eerste-divisie",
    "Italy": "https://www.thestatsdontlie.com/football/europe/italy/serie-a",
    "Poland": "https://www.thestatsdontlie.com/football/europe/poland/ekstraklasa",
    "Portugal": "https://www.thestatsdontlie.com/football/europe/portugal/primeira-liga",
    "Scotland": "https://www.thestatsdontlie.com/football/uk-ireland/scotland/premiership",
    "Spain1": "https://www.thestatsdontlie.com/football/europe/spain/la-liga",
    "Spain2": "https://www.thestatsdontlie.com/football/europe/spain/segunda-division",
    "Sweden": "https://www.thestatsdontlie.com/football/europe/sweden/allsvenskan",
    "Turkey": "https://www.thestatsdontlie.com/football/europe/turkey/super-lig",
    "USA": "https://www.thestatsdontlie.com/football/n-s-america/usa/mls"
}

TEAMS_IN_CHAMPIONSHIP = {
    "Australia": 12, "Austria": 12, "Belgium": 18, "Brazil": 20, "China": 16, "Croatia": 10, "Czech_Republic": 16,
    "Denmark": 12, "England1": 20, "England2": 24, "Finland": 12, "France1": 20, "France2": 20, "Germany1": 18,
    "Germany2": 18, "Holland1": 18, "Holland2": 20, "Italy": 20, "Poland": 18, "Portugal": 18, "Scotland": 12,
    "Spain1": 20, "Spain2": 22, "Sweden": 16, "Turkey": 20, "USA": 27
}

##### FOR GET ALL MATCHS #####
LIST_CHAMPIONSHIP = [
    "Australie : A-League", "Autriche : Bundesliga", "Belgique : Pro League", "Brésil : Série A",
    "Chine : Super League", "Croatie : 1. HNL", "République Tchèque : Ligue Tchèque", "Danemark : Superligaen",
    "Angleterre : Premier League", "Angleterre : League Championship", "Finlande : Veikkausliiga", "France : Ligue 1",
    "France : Ligue 2", "Allemagne : Bundesliga", "Allemagne : 2. Bundesliga", "Pays-Bas : Eredivisie",
    "Pays-Bas : Eerste Divisie", "Italie : Serie A", "Pologne : Ekstraklasa", "Portugal : Liga Sagres",
    "Écosse : Premier League", "Espagne : Liga BBVA", "Espagne : Liga Adelante", "Suède : Allsvenskan",
    "Turquie : Süper Lig", "Etats-Unis : Major League Soccer"]

#### CONVERSION #####
CONVERSION_LIST = {
    "Australie : A-League": "Australia",
    "Autriche : Bundesliga": "Austria",
    "Belgique : Pro League": "Belgium",
    "Brésil : Série A": "Brazil",
    "Chine : Super League": "China",
    "Croatie : 1. HNL": "Croatia",
    "République Tchèque : Ligue Tchèque": "Czech_Republic",
    "Danemark : Superligaen": "Denmark",
    "Angleterre : Premier League": "England1",
    "Angleterre : League Championship": "England2",
    "Finlande : Veikkausliiga": "Finland",
    "France : Ligue 1": "France1",
    "France : Ligue 2": "France2",
    "Allemagne : Bundesliga": "Germany1",
    "Allemagne : 2. Bundesliga": "Germany2",
    "Pays-Bas : Eredivisie": "Holland1",
    "Pays-Bas : Eerste Divisie": "Holland2",
    "Italie : Serie A": "Italy",
    "Pologne : Ekstraklasa": "Poland",
    "Portugal : Liga Sagres": "Portugal",
    "Écosse : Premier League": "Scotland",
    "Espagne : Liga BBVA": "Spain1",
    "Espagne : Liga Adelante": "Spain2",
    "Suède : Allsvenskan": "Sweden",
    "Turquie : Süper Lig": "Turkey",
    "Etats-Unis : Major League Soccer": "USA"
}

NEW_CONVERSION_LIST = {
    "Australie : A-League": "Australie - A-League",
    "Autriche : Bundesliga": "Autriche - Bundesliga",
    "Belgique : Pro League": "Belgique - Pro League",
    "Brésil : Série A": "Brésil - Série A",
    "Chine : Super League": "Chine - Super League",
    "Croatie : 1. HNL": "Croatie - 1. HNL",
    "République Tchèque : Ligue Tchèque": "République Tchèque - Ligue Tchèque",
    "Danemark : Superligaen": "Danemark - Superligaen",
    "Angleterre : Premier League": "Angleterre - Premier League",
    "Angleterre : League Championship": "Angleterre - League Championship",
    "Finlande : Veikkausliiga": "Finlande - Veikkausliiga",
    "France : Ligue 1": "France - Ligue 1",
    "France : Ligue 2": "France - Ligue 2",
    "Allemagne : Bundesliga": "Allemagne - Bundesliga",
    "Allemagne : 2. Bundesliga": "Allemagne - 2. Bundesliga",
    "Pays-Bas : Eredivisie": "Pays-Bas - Eredivisie",
    "Pays-Bas : Eerste Divisie": "Pays-Bas - Eerste Divisie",
    "Italie : Serie A": "Italie - Serie A",
    "Pologne : Ekstraklasa": "Pologne - Ekstraklasa",
    "Portugal : Liga Sagres": "Portugal - Liga Sagres",
    "Écosse : Premier League": "Écosse - Premier League",
    "Espagne : Liga BBVA": "Espagne - Liga BBVA",
    "Espagne : Liga Adelante": "Espagne - Liga Adelante",
    "Suède : Allsvenskan": "Suède - Allsvenskan",
    "Turquie : Süper Lig": "Turquie - Süper Lig",
    "Etats-Unis : Major League Soccer": "Etats-Unis - Major League Soccer"
}