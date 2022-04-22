import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from constant import LIST_CHAMPIONSHIP, CONVERSION_LIST
import os

all_matchs = {}


def open_browser():
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except:
        service = Service(executable_path="./chromedriver.exe")
    finally:
        driver = webdriver.Chrome(service=service)
    return driver


def get_all_matchs(date):
    url = f"https://www.matchendirect.fr/resultat-foot-{date}/"
    driver = open_browser()
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
                    format_match = f"{home_team_format}|{away_team_format}"
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
        .replace("Volendam", "FC Volendam").replace("Roda JC", "Roda").replace("AZ II", "Jong AZ")\
        .replace("Helmond Sport", "Helmond").replace("De Graafschap", "Graafschap").replace("NAC Breda", "Breda")\
        .replace("TOP Oss", "Oss").replace("FC Omniworld", "Almere").replace("FC Eindhoven", "Eindhoven")\
        .replace("Macarthur", "Macarthur FC").replace("Hrvatski Dragovoljac", "Dragovoljac")\
        .replace("Šibenik", 'Sibenik').replace("SønderjyskE", "Sonderjyske")\
        .replace("MKS Cracovia Cracovie", "Cracovia").replace("Zaglebie Lubin SSA", "Zaglebie")\
        .replace('KS Górnik Zabrze', "Gornik Z.").replace("Manchester United", "Man Utd").replace("Venise", "Venezia")\
        .replace("Inter Milan", "Inter").replace("Rome", "AS Roma").replace("Hellas Vérone", "Verona")\
        .replace("Eintracht Francfort", "Frankfurt").replace("Fribourg", "Freiburg")\
        .replace("Borussia M'gladbach", "Monchengladbach").replace("Cologne", "FC Koln")\
        .replace("Arminia Bielefeld", "Bielefeld").replace("Greuther Fürth", "Furth")\
        .replace("Bayer Leverkusen", "Leverkusen").replace("Bayern Munich", "Bayern")\
        .replace("Borussia Dortmund", "Dortmund").replace("Malines", "KV Mechelen")\
        .replace("Sporting Charleroi", "Charleroi").replace("Famalicão", "Famalicao")\
        .replace("Paços de Ferreira", "Ferreira").replace("Luton Town", "Luton").replace("Derby County", "Derby")\
        .replace("Hull City", "Hull").replace("Nottingham Forest", "Nottm Forest")\
        .replace("Sheffield United", "Sheff Utd").replace("Stoke City", "Stoke").replace("Queens Park Rangers", "QPR")\
        .replace("West Bromwich Albion", "West Brom").replace("Real Sociedad B", "R. Sociedad B")\
        .replace("Carthagène", "Cartagena").replace("Schalke 04", "Schalke").replace("Werder Brême", "Bremen")\
        .replace("Holstein Kiel", "Kiel").replace("Jahn Ratisbonne", "Regensburg").replace("Hambourg", "Hamburger SV")\
        .replace("Sankt Pau FCli", "St. Pauli").replace("Motherwell FC", "Motherwell")\
        .replace("Glasgow Rangers", "Rangers").replace("Livingston FC", "Livingston")\
        .replace("Saint Johnstone", "St. Johnstone").replace("Saint Mirren FC", "St. Mirren")\
        .replace("Fatih Karagümrük", "Karagumruk").replace("Gaziantep FK", "Gaziantep")\
        .replace("São Pau FClo", "Sao Paulo").replace("NEC", "Nijmegen")\
        .replace("Ajax Amsterdam", "Ajax").replace("AZ", "Alkmaar").replace("RKC Waalwijk", "Waalwijk")\
        .replace("PEC Zwolle", "Zwolle").replace("PSV Eindhoven", "PSV").replace("Linzer ASK", "LASK")\
        .replace("Rheindorf Altach", "Altach").replace("Wattens", "Tirol").replace("Lokomotiva Zagreb", "Lok. Zagreb")\
        .replace("Slask Wroclaw", "Slask").replace("Nieciecza", "Termalica B-B.").replace("GKS Piast Gliwice", "Piast")\
        .replace("Jagiellonia Bialystok SSA", "Jagiellonia").replace("OSP Lechia Gdansk", "Lechia")\
        .replace("KS Warta Poznan", "Warta").replace("Athletico PR", "Athletico-PR").replace("Wolverhampton", "Wolves")\
        .replace("Atlético Mineiro", "Atletico-MG").replace("América Mineiro", "America MG")\
        .replace("Cuiabá", "Cuiaba").replace("Augsbourg", "Augsburg").replace("Hertha Berlin", "Hertha")\
        .replace("Vitoria Guimaraes", "Guimaraes").replace("Alcorcón", "Alcorcon").replace("Real Oviedo", "R. Oviedo")\
        .replace("Ibiza", "UD Ibiza").replace("Mirandés", "Mirandes").replace("Real Valladolid", "Valladolid")\
        .replace("Real Saragosse", "Zaragoza").replace("Burgos", "Burgos CF").replace("Hanovre", "Hannover")\
        .replace("Nuremberg", "Nurnberg").replace("Erzgebirge Aue", "Aue").replace("Hansa Rostock", "Rostock")\
        .replace("Altay SK Izmir", "Altay").replace("Vitesse Arnheim", "Vitesse").replace("Fortuna Sittard", "Sittard")\
        .replace("Go Ahead Eagles", "G.A. Eagles").replace("ADO Den Haag", "Den Haag")\
        .replace("Utrecht II", "Jong Utrecht").replace("Slaven Koprivnica", "Slaven Belupo").replace("AaB", "Aalborg")\
        .replace("Nordsjælland", "Nordsjaelland").replace("FC Copenhague", "FC Copenhagen").replace("AGF", "Aarhus")\
        .replace("OB", "Odense").replace("KS FKS Stal Mielec", "Stal Mielec").replace("Legia Varsovie", "Legia")\
        .replace("Bologne", "Bologna").replace("Naples", "Napoli").replace("Club Bruges", "Club Brugge")\
        .replace("La Gantoise", "Gent").replace("Union Saint-Gilloise", "Royal Union SG")\
        .replace("Celtic Glasgow", "Celtic").replace("Dundee United FC", "Dundee Utd")\
        .replace("Heart of Midlothian FC", "Hearts").replace("Salzbourg", "Salzburg")\
        .replace("Austria Vienne", "Austria Vienna").replace("Austria Klagenfurt", "A. Klagenfurt")\
        .replace("Wolfsberger AC", "Wolfsberger").replace("Rapid Vienne", "Rapid Vienna")\
        .replace("Atlético GO", "Atletico GO").replace("Botafogo", "Botafogo RJ").replace("Juventus Turin", "Juventus")\
        .replace("Sporting Braga", "Braga").replace("Sporting CP", "Sporting").replace("Almería", "Almeria")\
        .replace("Sporting Gijón", "Gijon").replace("Kasimpasa SK", "Kasimpasa").replace("VVV", "Venlo")\
        .replace("MVV", "Maastricht").replace("Brøndby", "Brondby").replace("Wisla Cracovie SSA", "Wisla")\
        .replace("Wisla Plock SA", "Wisla Plock").replace("Preston North End", "Preston").replace('Avaí', "Avai")\
        .replace("Goiás", "Goias")


def format_championships_names(championship):
    return CONVERSION_LIST[championship]