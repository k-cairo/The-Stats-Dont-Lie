from datetime import date, timedelta, datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils.constant import LIST_CHAMPIONSHIP, CONVERSION_LIST
from utils.selenium_functions import open_browser, accept_cookie
from blog.models import MatchsAVenir, MatchsTermine

all_matchs = {}

today = datetime.today().strftime("%d-%m-%Y")
tomorrow = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
j2 = (date.today() + timedelta(days=2)).strftime("%d-%m-%Y")

day_list = (today, tomorrow, j2)


def get_all_matchs(date):
    """
    Get a date as input and return all matchs of this specified day
    :param date: str
    :return: {str: []}
    """
    all_matchs.clear()
    driver = open_browser()
    driver.get(f"https://www.matchendirect.fr/resultat-foot-{date}/")
    accept_cookie(driver=driver)

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
                    format_match = f"{home_team_format}|{away_team_format}"
                    all_matchs[championship_format].append(format_match)

    return all_matchs


def get_double_chance_predictions(day, ht, at):
    ht_format = format_team_names_2(ht)
    at_format = format_team_names_2(at)
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

        if home_team.lower() == ht_format.lower() or away_team.lower() == at_format.lower():
            double_chance_prediction = div_match.find_element(By.CSS_SELECTOR, 'div.tipdiv').text

            # For debugging
            if home_team.lower() != ht_format.lower():
                print(ht)
            if away_team.lower() != at_format.lower():
                print(at)

            return double_chance_prediction
    double_chance_prediction = ""
    return double_chance_prediction


def get_matchs_cards_goals(match, date, url):
    """
    Get the number of yellow cards, red cards and goals of the game passed as a parameter.
    Add this game in 'MatchsTermine' database and then delete this match from 'MatchsAVenir' database
    :param match: str
    :param date: str
    :param url: str
    :return: None
    """
    driver = open_browser()
    driver.get(url)

    goals = driver.find_elements(By.CSS_SELECTOR, "span.score")
    ht_goals = goals[0].text
    at_goals = goals[1].text

    nb_goals = int(ht_goals) + int(at_goals)
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
                                     nb_goals=nb_goals,
                                     score=f"{ht_goals} - {at_goals}",
                                     card_bet=new_query_values[0]['card_bet'])
        MatchsAVenir.objects.filter(date=date, match=match.replace("|", " - ")).delete()


def format_teams_names(team):
    """
    Return a copy with all occurrences of substring old replaced by new
    :param team: str
    :return: str
    """
    return team.replace("Paris Saint-Germain", "PSG").replace("Manchester City", "Man City") \
        .replace("Espanyol Barcelone", "Espanyol").replace("Séville", "Sevilla").replace("Cadix", "Cadiz") \
        .replace("Athletic Bilbao", 'Ath. Bilbao').replace("Barcelone", "Barcelona").replace("Värnamo", "Varnamo") \
        .replace("Malmö FF", "Malmo FF").replace("St Étienne", "St. Etienne").replace("Grenade", "Granada") \
        .replace("Atlético Madrid", "Atl. Madrid").replace('Western Sydney Wanderers', "WS Wanderers") \
        .replace("Dinamo Zagreb", "Din. Zagreb").replace("KKS Lech Poznan", "Lech") \
        .replace("GKS Górnik Leczna SA", "Leczna").replace("MKS Pogon Szczecin", "Pogon Szczecin") \
        .replace("Raków Czestochowa", "Rakow").replace("Bohemians 1905", "Bohemians") \
        .replace("Hradec Králové", "Hradec Kralove").replace("Mladá Boleslav", "Mlada Boleslav") \
        .replace("Viktoria Plzeň", "Plzen").replace("České Budějovice", "Ceske Budejovice") \
        .replace("Karviná", "Karvina").replace("FK Pardubice", "Pardubice").replace("Zlín", "Zlin") \
        .replace("Baník Ostrava", "Ostrava").replace("Slovácko", "Slovacko").replace("Slovan Liberec", "Liberec") \
        .replace("AIK", "AIK Stockholm").replace("Varberg", "Varbergs").replace("IFK Göteborg", "Goteborg") \
        .replace("Djurgården", "Djurgarden").replace("Norrköping", "Norrkoping").replace("Häcken", "Hacken") \
        .replace("Mjällby", "Mjallby").replace("GIF Sundsvall", "Sundsvall").replace("Amiens SC", "Amiens") \
        .replace("Quevilly", "Quevilly Rouen").replace("Nîmes", "Nimes").replace("Pau", "Pau FC") \
        .replace("Ajaccio", "AC Ajaccio").replace("Wolfsbourg", "Wolfsburg").replace("Mayence", "Mainz") \
        .replace("Huddersfield Town", "Huddersfield").replace("Fortuna Düsseldorf", "Dusseldorf") \
        .replace("Dynamo Dresde", "Dresden").replace("Karlsruhe", "Karlsruher").replace("Caykur Rizespor", "Rizespor") \
        .replace("Volendam", "FC Volendam").replace("Roda JC", "Roda").replace("AZ II", "Jong AZ") \
        .replace("Helmond Sport", "Helmond").replace("De Graafschap", "Graafschap").replace("NAC Breda", "Breda") \
        .replace("TOP Oss", "Oss").replace("FC Omniworld", "Almere").replace("FC Eindhoven", "Eindhoven") \
        .replace("Macarthur", "Macarthur FC").replace("Hrvatski Dragovoljac", "Dragovoljac") \
        .replace("Šibenik", 'Sibenik').replace("SønderjyskE", "Sonderjyske") \
        .replace("MKS Cracovia Cracovie", "Cracovia").replace("Zaglebie Lubin SSA", "Zaglebie") \
        .replace('KS Górnik Zabrze', "Gornik Z.").replace("Manchester United", "Man Utd").replace("Venise", "Venezia") \
        .replace("Inter Milan", "Inter").replace("Rome", "AS Roma").replace("Hellas Vérone", "Verona") \
        .replace("Eintracht Francfort", "Frankfurt").replace("Fribourg", "Freiburg") \
        .replace("Borussia M'gladbach", "Monchengladbach").replace("Cologne", "FC Koln") \
        .replace("Arminia Bielefeld", "Bielefeld").replace("Greuther Fürth", "Furth") \
        .replace("Bayer Leverkusen", "Leverkusen").replace("Bayern Munich", "Bayern") \
        .replace("Borussia Dortmund", "Dortmund").replace("Malines", "KV Mechelen") \
        .replace("Sporting Charleroi", "Charleroi").replace("Famalicão", "Famalicao") \
        .replace("Paços de Ferreira", "Ferreira").replace("Luton Town", "Luton").replace("Derby County", "Derby") \
        .replace("Hull City", "Hull").replace("Nottingham Forest", "Nottm Forest") \
        .replace("Sheffield United", "Sheff Utd").replace("Stoke City", "Stoke").replace("Queens Park Rangers", "QPR") \
        .replace("West Bromwich Albion", "West Brom").replace("Real Sociedad B", "R. Sociedad B") \
        .replace("Carthagène", "Cartagena").replace("Schalke 04", "Schalke").replace("Werder Brême", "Bremen") \
        .replace("Holstein Kiel", "Kiel").replace("Jahn Ratisbonne", "Regensburg").replace("Hambourg", "Hamburger SV") \
        .replace("Sankt Pau FCli", "St. Pauli").replace("Motherwell FC", "Motherwell") \
        .replace("Glasgow Rangers", "Rangers").replace("Livingston FC", "Livingston") \
        .replace("Saint Johnstone", "St. Johnstone").replace("Saint Mirren FC", "St. Mirren") \
        .replace("Fatih Karagümrük", "Karagumruk").replace("Gaziantep FK", "Gaziantep") \
        .replace("São Pau FClo", "Sao Paulo").replace("NEC", "Nijmegen") \
        .replace("Ajax Amsterdam", "Ajax").replace("AZ", "Alkmaar").replace("RKC Waalwijk", "Waalwijk") \
        .replace("PEC Zwolle", "Zwolle").replace("PSV Eindhoven", "PSV").replace("Linzer ASK", "LASK") \
        .replace("Rheindorf Altach", "Altach").replace("Wattens", "Tirol").replace("Lokomotiva Zagreb", "Lok. Zagreb") \
        .replace("Slask Wroclaw", "Slask").replace("Nieciecza", "Termalica B-B.").replace("GKS Piast Gliwice", "Piast") \
        .replace("Jagiellonia Bialystok SSA", "Jagiellonia").replace("OSP Lechia Gdansk", "Lechia") \
        .replace("KS Warta Poznan", "Warta").replace("Athletico PR", "Athletico-PR").replace("Wolverhampton", "Wolves") \
        .replace("Atlético Mineiro", "Atletico-MG").replace("América Mineiro", "America MG") \
        .replace("Cuiabá", "Cuiaba").replace("Augsbourg", "Augsburg").replace("Hertha Berlin", "Hertha") \
        .replace("Vitoria Guimaraes", "Guimaraes").replace("Alcorcón", "Alcorcon").replace("Real Oviedo", "R. Oviedo") \
        .replace("Ibiza", "UD Ibiza").replace("Mirandés", "Mirandes").replace("Real Valladolid", "Valladolid") \
        .replace("Real Saragosse", "Zaragoza").replace("Burgos", "Burgos CF").replace("Hanovre", "Hannover") \
        .replace("Nuremberg", "Nurnberg").replace("Erzgebirge Aue", "Aue").replace("Hansa Rostock", "Rostock") \
        .replace("Altay SK Izmir", "Altay").replace("Vitesse Arnheim", "Vitesse").replace("Fortuna Sittard", "Sittard") \
        .replace("Go Ahead Eagles", "G.A. Eagles").replace("ADO Den Haag", "Den Haag") \
        .replace("Utrecht II", "Jong Utrecht").replace("Slaven Koprivnica", "Slaven Belupo").replace("AaB", "Aalborg") \
        .replace("Nordsjælland", "Nordsjaelland").replace("FC Copenhague", "FC Copenhagen").replace("AGF", "Aarhus") \
        .replace("OB", "Odense").replace("KS FKS Stal Mielec", "Stal Mielec").replace("Legia Varsovie", "Legia") \
        .replace("Bologne", "Bologna").replace("Naples", "Napoli").replace("Club Bruges", "Club Brugge") \
        .replace("La Gantoise", "Gent").replace("Union Saint-Gilloise", "Royal Union SG") \
        .replace("Celtic Glasgow", "Celtic").replace("Dundee United FC", "Dundee Utd") \
        .replace("Heart of Midlothian FC", "Hearts").replace("Salzbourg", "Salzburg") \
        .replace("Austria Vienne", "Austria Vienna").replace("Austria Klagenfurt", "A. Klagenfurt") \
        .replace("Wolfsberger AC", "Wolfsberger").replace("Rapid Vienne", "Rapid Vienna") \
        .replace("Atlético GO", "Atletico GO").replace("Botafogo", "Botafogo RJ").replace("Juventus Turin", "Juventus") \
        .replace("Sporting Braga", "Braga").replace("Sporting CP", "Sporting").replace("Almería", "Almeria") \
        .replace("Sporting Gijón", "Gijon").replace("Kasimpasa SK", "Kasimpasa").replace("VVV", "Venlo") \
        .replace("MVV", "Maastricht").replace("Brøndby", "Brondby").replace("Wisla Cracovie SSA", "Wisla") \
        .replace("Wisla Plock SA", "Wisla Plock").replace("Preston North End", "Preston").replace('Avaí', "Avai") \
        .replace("Goiás", "Goias").replace("Montréal Impact", "CF Montreal").replace("Los Angeles", "Los Angeles FC") \
        .replace("LA Galaxy", "Los Angeles Galaxy").replace("SJ Earthquakes", "San Jose Earthquakes") \
        .replace("Minnesota United", "Minnesota").replace("Austin", "Austin FC") \
        .replace("New England", "New England Revolution").replace('New York RB', "New York Red Bulls") \
        .replace("Toronto", "Toronto FC").replace("Dallas", "FC Dallas").replace("Sporting KC", "Sporting Kansas City") \
        .replace("Whitecaps", "Vancouver Whitecaps").replace("Alavés", "Alaves").replace("Majorque", "Mallorca")\
        .replace("Vejle-Kolding", "Vejle").replace("Ferreira", "Pacos Ferreira")\
        .replace("Quevilly Rouen-Rouen", "Quevilly Rouen").replace("Ceará", "Ceara").replace("Real Bétis", "Betis")\
        .replace("Philadelphie Union", "Philadelphia Union").replace("Valence", "Valencia")


def format_team_names_2(team):
    return team.replace('Jagiellonia', 'Jagiellonia Bialystok').replace("Legia", "Legia Warsaw")\
        .replace("Dragovoljac", "NK Hrvatski Dragovoljac").replace("Gorica", "HNK Gorica")\
        .replace("Atletico-MG", "Atletico Mineiro").replace("Aarhus", "AGF Aarhus").replace("Odense", "Odense BK")\
        .replace("Cracovia", "Cracovia Krakow").replace("St. Etienne", "St Etienne")\
        .replace("Clermont", "Clermont Foot").replace("AS Roma", "Roma").replace("Bayern", "Bayern Munich")\
        .replace("Frankfurt", "Eintracht Frankfurt").replace("Furth", "Greuther Furth")\
        .replace("Bielefeld", "Arminia Bielefeld").replace("Arouca", "FC Arouca")\
        .replace("Orlando City", "Orlando City SC").replace("Western United", "Western United FC")\
        .replace("Tirol", "WSG Swarovski Tirol").replace("Rijeka", "HNK Rijeka").replace("Lechia", "Lechia Gdansk")\
        .replace("Dortmund", "Borussia Dortmund").replace("Hertha", "Hertha Berlin")\
        .replace("Leverkusen", "Bayer Leverkusen").replace("Freiburg", "SC Freiburg")\
        .replace("Monchengladbach", "Borussia M'gladbach").replace("Hoffenheim", "TSG Hoffenheim")\
        .replace("Stuttgart", "VfB Stuttgart").replace("FC Koln", "Cologne").replace("Ried", "SV Ried")\
        .replace("LASK", "LASK Linz").replace("Admira", "FC Flyeralarm Admira").replace("Altach", "SCR Altach")\
        .replace("Termalica B-B.", "Termalica BB Nieciecza").replace("Piast", "Piast Gliwice")\
        .replace("Warta", "Warta Poznan").replace("Lech", "Lech Poznan").replace("Zaglebie", "Zaglebie Lubin")\
        .replace("Rakow", "Rakow Czestochowa").replace("Mjallby", "Mjällby AIF").replace("Varnamo", "IFK Varnamo")


def format_championships_names(championship):
    return CONVERSION_LIST[championship]

