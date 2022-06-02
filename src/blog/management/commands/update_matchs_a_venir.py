from django.core.management.base import BaseCommand
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from slugify import slugify
from utils.constant import day_list, LIST_CHAMPIONSHIP, CONVERSION_LIST
from utils.selenium_functions import open_browser, accept_cookie
from blog.models import MatchsAVenir, Data


def get_all_matchs(date):
    all_matchs = {}
    driver = open_browser()
    driver.get(f"https://www.matchendirect.fr/resultat-foot-{date}/")
    accept_cookie(driver=driver)

    all_div_championships = driver.find_elements(By.CSS_SELECTOR, "div div.panel.panel-info")

    for div_championship in all_div_championships[:-2]:
        try:
            championship = div_championship.find_element(By.CSS_SELECTOR, "h3.panel-title a").text
        except NoSuchElementException:
            pass
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


def format_championships_names(championship):
    return CONVERSION_LIST[championship]


def format_teams_names(team):
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
        .replace("Whitecaps", "Vancouver Whitecaps").replace("Alavés", "Alaves").replace("Majorque", "Mallorca") \
        .replace("Vejle-Kolding", "Vejle").replace("Ferreira", "Pacos Ferreira") \
        .replace("Quevilly Rouen-Rouen", "Quevilly Rouen").replace("Ceará", "Ceara").replace("Real Bétis", "Betis") \
        .replace("Philadelphie Union", "Philadelphia Union").replace("Valence", "Valencia") \
        .replace("Melbourne Heart", "Melbourne City")


def get_cards_queryset(championship):
    card_for_query = Data.objects.filter(championship=championship).filter(datas_stats="cards for")
    card_against_query = Data.objects.filter(championship=championship).filter(datas_stats="cards against")

    card_for_query_values = card_for_query.values()
    card_against_query_values = card_against_query.values()

    return card_for_query_values, card_against_query_values


def get_corners_queryset(championship):
    corner_for_query = Data.objects.filter(championship=championship).filter(datas_stats="corners for")
    corner_against_query = Data.objects.filter(championship=championship).filter(datas_stats="corners against")

    corner_for_query_values = corner_for_query.values()
    corner_against_query_values = corner_against_query.values()

    return corner_for_query_values, corner_against_query_values


def get_home_away_team_cards_stats(cards_querysets, home_team, away_team):
    home_team_cards_for_average = 0
    home_team_cards_against_average = 0
    away_team_cards_for_average = 0
    away_team_cards_against_average = 0

    for data_tuple in cards_querysets[0][0]["datas"]["Home Teams"]:
        for team, cards_average in data_tuple.items():
            if team == home_team:
                home_team_cards_for_average = float(cards_average)

    for data_tuple in cards_querysets[1][0]["datas"]["Home Teams"]:
        for team, cards_average in data_tuple.items():
            if team == home_team:
                home_team_cards_against_average = float(cards_average)

    for data_tuple in cards_querysets[0][0]["datas"]["Away Teams"]:
        for team, cards_average in data_tuple.items():
            if team == away_team:
                away_team_cards_for_average = float(cards_average)

    for data_tuple in cards_querysets[1][0]["datas"]["Away Teams"]:
        for team, cards_average in data_tuple.items():
            if team == away_team:
                away_team_cards_against_average = float(cards_average)

    return home_team_cards_for_average, home_team_cards_against_average, away_team_cards_for_average, away_team_cards_against_average


def get_home_away_team_corners_stats(corners_querysets, home_team, away_team):
    home_team_corners_for_average = 0
    home_team_corners_against_average = 0
    away_team_corners_for_average = 0
    away_team_corners_against_average = 0

    for data_tuple in corners_querysets[0][0]["datas"]["Home Teams"]:
        for team, corners_average in data_tuple.items():
            if team == home_team:
                home_team_corners_for_average = float(corners_average)

    for data_tuple in corners_querysets[1][0]["datas"]["Home Teams"]:
        for team, corners_average in data_tuple.items():
            if team == home_team:
                home_team_corners_against_average = float(corners_average)

    for data_tuple in corners_querysets[0][0]["datas"]["Away Teams"]:
        for team, corners_average in data_tuple.items():
            if team == away_team:
                away_team_corners_for_average = float(corners_average)

    for data_tuple in corners_querysets[1][0]["datas"]["Away Teams"]:
        for team, corners_average in data_tuple.items():
            if team == away_team:
                away_team_corners_against_average = float(corners_average)

    return home_team_corners_for_average, home_team_corners_against_average, away_team_corners_for_average, away_team_corners_against_average


def calculate_total_stats(home_team_stats_for_average, away_team_stats_for_average, home_team_stats_ag_average,
                          away_team_stats_ag_average):
    return min(home_team_stats_for_average, away_team_stats_for_average) + min(
        home_team_stats_ag_average, away_team_stats_ag_average)


def define_stat_bet(total_stats):
    if total_stats >= 13.5:
        return "+ 12.5"
    elif total_stats >= 12.5:
        return "+ 11.5"
    elif total_stats >= 11.5:
        return "+ 10.5"
    elif total_stats >= 10.5:
        return "+ 9.5"
    elif total_stats >= 9.5:
        return "+ 8.5"
    elif total_stats >= 8.5:
        return "+ 7.5"
    elif total_stats >= 7.5:
        return "+ 6.5"
    elif total_stats >= 6.5:
        return "+ 5.5"
    elif total_stats >= 5.5:
        return "+ 4.5"
    elif total_stats >= 4.5:
        return "+ 3.5"
    elif total_stats >= 3.5:
        return "+ 2.5"
    elif total_stats >= 2.5:
        return "+ 1.5"
    elif total_stats >= 1.5:
        return "+ 0.5"
    else:
        return "+0"


def create_match_in_database(rencontre, championship, day, all_teams_cards_stats, all_teams_corners_stats, card_bet,
                             corner_bet):
    return MatchsAVenir.objects.create(match=rencontre.replace('|', ' - '),
                                       championship=championship,
                                       date=day,
                                       slug=slugify(rencontre),
                                       home_team=rencontre.split("|")[0],
                                       away_team=rencontre.split("|")[1],
                                       home_team_cards_for_average=all_teams_cards_stats[0],
                                       home_team_cards_against_average=all_teams_cards_stats[1],
                                       away_team_cards_for_average=all_teams_cards_stats[2],
                                       away_team_cards_against_average=all_teams_cards_stats[3],
                                       home_team_corners_for_average=all_teams_corners_stats[0],
                                       home_team_corners_against_average=all_teams_corners_stats[1],
                                       away_team_corners_for_average=all_teams_corners_stats[2],
                                       away_team_corners_against_average=all_teams_corners_stats[3],
                                       card_bet=card_bet,
                                       corner_bet=corner_bet)


class Command(BaseCommand):
    help = 'Update Match a venir'

    def handle(self, *args, **options):
        # Check if day already in database (Next 3 days)
        for day in day_list:
            data_dates = MatchsAVenir.objects.filter(date=day)
            if len(data_dates) == 0:
                all_match = get_all_matchs(day)

                for championship, rencontres in all_match.items():
                    for rencontre in rencontres:
                        if not MatchsAVenir.objects.filter(match=rencontre.replace('|', ' - '), date=day).exists():
                            teams = rencontre.split("|")
                            home_team = teams[0]
                            away_team = teams[1]

                            # GET CARDS AND CORNERS QUERYSETS
                            cards_querysets = get_cards_queryset(championship=championship)
                            corners_querysets = get_corners_queryset(championship=championship)

                            # GET ALL TEAMS CARDS AND CORNERS STATS
                            all_teams_cards_stats = get_home_away_team_cards_stats(cards_querysets, home_team,
                                                                                   away_team)
                            all_teams_corners_stats = get_home_away_team_corners_stats(corners_querysets, home_team,
                                                                                       away_team)

                            # CALCULATE TOTAL CARDS AND TOTAL CORNERS
                            tot_cards = calculate_total_stats(home_team_stats_for_average=all_teams_cards_stats[0],
                                                              away_team_stats_for_average=all_teams_cards_stats[2],
                                                              home_team_stats_ag_average=all_teams_cards_stats[1],
                                                              away_team_stats_ag_average=all_teams_cards_stats[3])
                            tot_corners = calculate_total_stats(home_team_stats_for_average=all_teams_corners_stats[0],
                                                                away_team_stats_for_average=all_teams_corners_stats[2],
                                                                home_team_stats_ag_average=all_teams_corners_stats[1],
                                                                away_team_stats_ag_average=all_teams_corners_stats[3])

                            # DEFINE CARD AND CORNER BET
                            card_bet = define_stat_bet(total_stats=tot_cards)
                            corner_bet = define_stat_bet(total_stats=tot_corners)

                            # CREATE MATCH A VENIR IN DATABASE
                            create_match_in_database(rencontre=rencontre,
                                                     championship=championship,
                                                     day=day,
                                                     all_teams_cards_stats=all_teams_cards_stats,
                                                     all_teams_corners_stats=all_teams_corners_stats,
                                                     card_bet=card_bet,
                                                     corner_bet=corner_bet)

        self.stdout.write('Match a venir Updated Successfully')
