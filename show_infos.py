import json


def debug_format_teams(champ, ht, at):
    ht_cards_for = 0
    at_cards_for = 0

    with open(f'./data/{champ}/{champ}_cards_for.json', "r") as f:
        content = json.load(f)

    print(champ)
    print(f"{ht} - {at}")

    home_teams = content["Home Teams"]
    for element in home_teams:
        if element.get(ht) is not None:
            ht_cards_for = element.get(ht)
            print(f"{ht} - {ht_cards_for} Cards For")

    away_teams = content["Away Teams"]
    for element in away_teams:
        if element.get(at) is not None:
            at_cards_for = element.get(at)
            print(f"{at} - {at_cards_for} Cards For")

    print("-" * 50)


def get_card_for(champ, ht, at):
    ht_cards_for = 0
    at_cards_for = 0

    with open(f'./data/{champ}/{champ}_cards_for.json', "r") as f:
        content = json.load(f)

    home_teams = content["Home Teams"]
    for element in home_teams:
        if element.get(ht) is not None:
            ht_cards_for = element.get(ht)

    away_teams = content["Away Teams"]
    for element in away_teams:
        if element.get(at) is not None:
            at_cards_for = element.get(at)

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
