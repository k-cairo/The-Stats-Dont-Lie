from django.shortcuts import render
from utils.constant import LOGO_LIST, day_list, today, tomorrow, j2
from .models import MatchsAVenir, Data, MatchsTermine
from django.db.models import Q


def index(request):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))
    context = {"matchs": today_j3_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def today_matchs(request):
    today_matchs = MatchsAVenir.objects.filter(date=today)
    context = {"matchs": today_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def tomorrow_matchs(request):
    tomorrow_matchs = MatchsAVenir.objects.filter(date=tomorrow)
    context = {"matchs": tomorrow_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def j2_matchs(request):
    j2_matchs = MatchsAVenir.objects.filter(date=j2)
    context = {"matchs": j2_matchs, "logo": LOGO_LIST}
    return render(request, "blog/index.html", context=context)


def match_details(request, slug):
    today_j3_matchs = MatchsAVenir.objects.filter(Q(date=today) | Q(date=tomorrow) | Q(date=j2))

    for match in today_j3_matchs:
        if match.slug == slug:
            target_match = match

            championship = target_match.championship
            home_team = target_match.home_team
            away_team = target_match.away_team

            home_team_histo = MatchsTermine.objects.filter(target_team=home_team)
            away_team_histo = MatchsTermine.objects.filter(target_team=away_team)

            cards_for_data = Data.objects.filter(championship=championship).filter(datas_stats="cards for").get().datas
            cards_against_data = Data.objects.filter(championship=championship).filter(datas_stats="cards against").get().datas

            home_team_cards_for_average = 0
            away_team_cards_for_average = 0
            home_team_cards_against_average = 0
            away_team_cards_against_average = 0

            for data1 in cards_for_data["Home Teams"]:
                for team1, average_card1 in data1.items():
                    if team1 == home_team:
                        home_team_cards_for_average = average_card1
                        print(home_team_cards_for_average)

            for data2 in cards_for_data["Away Teams"]:
                for team2, average_card2 in data2.items():
                    if team2 == away_team:
                        away_team_cards_for_average = average_card2

            for data3 in cards_against_data["Home Teams"]:
                for team3, average_card3 in data3.items():
                    if team3 == home_team:
                        home_team_cards_against_average = average_card3
                        print(home_team_cards_against_average)

            for data4 in cards_against_data["Away Teams"]:
                for team4, average_card4 in data4.items():
                    if team4 == away_team:
                        away_team_cards_against_average = average_card4

    return render(request, "blog/match_details.html", context={"home_team_histo": home_team_histo,
                                                               "away_team_histo": away_team_histo,
                                                               "home_team": home_team,
                                                               "away_team": away_team,
                                                               "target_match": target_match,
                                                               "home_team_cards_for_average": home_team_cards_for_average,
                                                               "away_team_cards_for_average": away_team_cards_for_average,
                                                               "home_team_cards_against_average": home_team_cards_against_average,
                                                               "away_team_cards_against_average": away_team_cards_against_average})
