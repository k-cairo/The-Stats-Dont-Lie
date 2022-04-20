import json
from datetime import datetime, timedelta, date


def read_match_list():
    tomorrow = date.today() + timedelta(days=1)
    tomorrow_format = tomorrow.strftime("%d-%m-%Y")
    today = datetime.today().strftime("%d-%m-%Y")

    user_date = input("Vous voulez les statistiques pour quel jour?(au format JJ-MM-AAAA ou Aujourd'hui et Demain): ")

    if user_date.lower() == "aujourd'hui":
        user_date = today
    elif user_date.lower() == "demain":
        user_date = tomorrow_format

    with open(f"./Liste de Matchs/{user_date}.json", "r") as f:
        matchs_list = json.load(f)

    for championship in matchs_list:
        matchs = matchs_list[championship]
        for match in matchs:
            match_split = match.split("-")
            home_team = match_split[0]
            away_team = match_split[1]
            cards_for_stats = get_card_for(champ=championship, ht=home_team, at=away_team)
            cards_against_stats = get_card_against(champ=championship, ht=home_team, at=away_team)
            corners_for_stats = get_corner_for(champ=championship, ht=home_team, at=away_team)
            corners_against_stats = get_corner_against(champ=championship, ht=home_team, at=away_team)
            show_stats(match=match, cards_for=cards_for_stats, cards_against=cards_against_stats,
                       corners_for=corners_for_stats, corners_against=corners_against_stats)


def show_stats(match, cards_for, cards_against, corners_for, corners_against):
    print(match)
    print(f"{cards_for} Cards For")
    print(f"{cards_against} Cards Against")
    print(f"{corners_for} Corners For")
    print(f"{corners_against} Corners Against")
    print("-"*50)


def get_card_for(champ, ht, at):
    ht_cards_for = 0
    at_cards_for = 0

    with open(f'./data/{champ}/{champ}_cards_for.json', "r") as f:
        content = json.load(f)

    # print(champ)
    # print(f"{ht} - {at}")

    home_teams = content["Home Teams"]
    for element in home_teams:
        if element.get(ht) is not None:
            ht_cards_for = element.get(ht)
            # print(f"{ht} - {ht_cards_for} Cards For")

    away_teams = content["Away Teams"]
    for element in away_teams:
        if element.get(at) is not None:
            at_cards_for = element.get(at)
            # print(f"{at} - {at_cards_for} Cards For")

    # print("-"*50)

    return min(float(ht_cards_for), float(at_cards_for))


def get_card_against(champ, ht, at):
    ht_cards_against = 0
    at_cards_against = 0

    with open(f'./data/{champ}/{champ}_cards_against.json', "r") as f:
        content = json.load(f)

    home_teams = content["Home Teams"]
    for element in home_teams:
        if element.get(ht) is not None:
            ht_cards_against = element.get(ht)

    away_teams = content["Away Teams"]
    for element in away_teams:
        if element.get(at) is not None:
            at_cards_against = element.get(at)

    return min(float(ht_cards_against), float(at_cards_against))


def get_corner_for(champ, ht, at):
    ht_corners_for = 0
    at_corners_for = 0

    with open(f'./data/{champ}/{champ}_corners_for.json', "r") as f:
        content = json.load(f)

    home_teams = content["Home Teams"]
    for element in home_teams:
        if element.get(ht) is not None:
            ht_corners_for = element.get(ht)

    away_teams = content["Away Teams"]
    for element in away_teams:
        if element.get(at) is not None:
            at_corners_for = element.get(at)

    return min(float(ht_corners_for), float(at_corners_for))


def get_corner_against(champ, ht, at):
    ht_corners_against = 0
    at_corners_against = 0

    with open(f'./data/{champ}/{champ}_corners_against.json', "r") as f:
        content = json.load(f)

    home_teams = content["Home Teams"]
    for element in home_teams:
        if element.get(ht) is not None:
            ht_corners_against = element.get(ht)

    away_teams = content["Away Teams"]
    for element in away_teams:
        if element.get(at) is not None:
            at_corners_against = element.get(at)

    return min(float(ht_corners_against), float(at_corners_against))


if __name__ == "__main__":
    read_match_list()