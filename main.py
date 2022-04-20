import json
import get_iframes, get_data, get_matchs
import os

YELLOW_CARD_FOR_PATH = "./iframes/cards/iframes_cards_for.json"
YELLOW_CARD_AGAINST_PATH = "./iframes/cards/iframes_cards_against.json"
FULL_TIME_CORNER_FOR = "./iframes/corners/iframes_corners_for.json"
FULL_TIME_CORNER_AGAINST = "./iframes/corners/iframes_corners_against.json"

ALL_PATHS = [YELLOW_CARD_AGAINST_PATH, YELLOW_CARD_FOR_PATH, FULL_TIME_CORNER_AGAINST, FULL_TIME_CORNER_FOR]


##### GET ALL IFRAMES (Cards & Corners) #####
# get_iframes.get_all_cards_iframes()
# get_iframes.get_all_corners_iframes()
get_iframes.driver.close()


##### GET ALL DATAS #####
# for path in ALL_PATHS:
#     if os.path.exists(path):
#         with open(path) as f:
#             data = json.load(f)
#             for championship, iframe in data.items():
#                 get_data.get_data(url=iframe, championship=championship, path_iframe=path)
get_data.driver.close()

##### GET ALL MATCHS ##### # OK
get_matchs.get_user_date()

##### SHOW FORMAT DATA ##### TODO