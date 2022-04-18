import json
import get_iframe, get_data
import os

YELLOW_CARD_FOR_PATH = "./iframes/cards/iframes_cards_for.json"
YELLOW_CARD_AGAINST_PATH = "./iframes/cards/iframes_cards_against.json"
FULL_TIME_CORNER_FOR = "./iframes/corners/iframes_corners_for.json"
FULL_TIME_CORNER_AGAINST = "./iframes/corners/iframes_corners_against.json"

ALL_PATHS = [YELLOW_CARD_AGAINST_PATH, YELLOW_CARD_FOR_PATH, FULL_TIME_CORNER_AGAINST, FULL_TIME_CORNER_FOR]

##### GET ALL IFRAMES (Cards & Corners) #####
# get_iframe.get_all_cards_iframes()  OK
# get_iframe.get_all_corners_iframes() OK

##### GET ALL DATAS ##### TODO
for path in ALL_PATHS:
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
            for championship, iframe in data.items():
                get_data.get_data(url=iframe, championship=championship)