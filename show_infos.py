import json


def read_match_list():
    with open("./Liste de Matchs/Tuesday 19 April 2022.json", "r") as f:
        matchs_list = json.load(f)

    for championship in matchs_list:
        matchs = matchs_list[championship]
        for match in matchs:
            match_split = match.split("-")
            home_team = match_split[0]
            away_team = match_split[1]
            show_card_for(champ=championship, ht=home_team, at=away_team)
            # print(f"{championship} - {match}")


def show_card_for(champ, ht, at):
    with open(f'./data/{champ}/{champ}_cards_for.json', "r") as f:
        content = json.load(f)

    # Home Team DATA
    home_teams = content["Home Teams"]
    for element in home_teams:
        if not element.get(ht) is None:
            print(f"{ht} - {element.get(ht)} Cards For")

    # Away Team DATA
    away_teams = content["Away Teams"]
    for element in away_teams:
        if not element.get(at) is None:
            print(f"{at} - {element.get(at)} Cards For")


def show_card_against(champ, ht, at):
    with open(f'./data/{champ}/{champ}_cards_against.json', "r") as f:
        content = json.load(f)


def show_corner_for(champ, ht, at):
    with open(f'./data/{champ}/{champ}_corners_for.json', "r") as f:
        content = json.load(f)


def show_corner_against(champ, ht, at):
    with open(f'./data/{champ}/{champ}_corners_against.json', "r") as f:
        content = json.load(f)
