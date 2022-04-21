from datetime import datetime, timedelta, date
from functools import partial
from tkinter import Tk, Button, Label, Text, END
import get_data
import get_iframes
import get_matchs
import show_infos
import json

today = datetime.today().strftime("%d-%m-%Y")
tomorrow = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
j2 = (date.today() + timedelta(days=2)).strftime("%d-%m-%Y")
j3 = (date.today() + timedelta(days=3)).strftime("%d-%m-%Y")
j4 = (date.today() + timedelta(days=4)).strftime("%d-%m-%Y")
j5 = (date.today() + timedelta(days=5)).strftime("%d-%m-%Y")


class UserInterface:
    BUTTONS_WIDTH = 29
    LEFT_RIGHT_BUTTONS_HEIGHT = 8

    def __init__(self):
        self.window = Tk()
        self.window.title("Statistiques Corners & Cartons")
        self.window.geometry("1070x465")

        # Label
        self.main_label = Label(text="Statistiques Corners & Cartons", )
        self.main_label.grid(row=0, column=0, columnspan=5)

        # Left Buttons GET
        self.get_cards_iframes_button = Button(
            text="Get Cards Iframes",
            command=get_iframes.get_all_cards_iframes,
            width=UserInterface.BUTTONS_WIDTH,
            height=UserInterface.LEFT_RIGHT_BUTTONS_HEIGHT)
        self.get_cards_iframes_button.grid(row=1, column=0)

        self.get_corners_iframes_button = Button(
            text="Get Corners Iframes",
            command=get_iframes.get_all_corners_iframes,
            width=UserInterface.BUTTONS_WIDTH,
            height=UserInterface.LEFT_RIGHT_BUTTONS_HEIGHT)
        self.get_corners_iframes_button.grid(row=2, column=0)

        self.get_datas_button = Button(
            text="Get Datas",
            command=get_data.get_all_datas,
            width=UserInterface.BUTTONS_WIDTH,
            height=UserInterface.LEFT_RIGHT_BUTTONS_HEIGHT)
        self.get_datas_button.grid(row=3, column=0)

        # Right Buttons VIEW #TODO (ALL COMMANDS)
        self.view_cards_iframes_button = Button(
            text="View Cards Iframes\nComing Next",
            state="disabled",
            width=UserInterface.BUTTONS_WIDTH,
            height=UserInterface.LEFT_RIGHT_BUTTONS_HEIGHT)
        self.view_cards_iframes_button.grid(row=1, column=4)

        self.view_corners_iframes_button = Button(
            text="View Corners Iframes\nComing Next",
            state="disabled",
            width=UserInterface.BUTTONS_WIDTH,
            height=UserInterface.LEFT_RIGHT_BUTTONS_HEIGHT)
        self.view_corners_iframes_button.grid(row=2, column=4)

        self.view_datas_button = Button(
            text="View Datas\nComing Next",
            state="disabled",
            width=UserInterface.BUTTONS_WIDTH,
            height=UserInterface.LEFT_RIGHT_BUTTONS_HEIGHT)
        self.view_datas_button.grid(row=3, column=4)

        # Bottom Buttons GET
        self.get_todays_matchs_button = Button(
            text=f"Get Matchs : {datetime.today().strftime('%A %d %B')}",
            command=partial(get_matchs.get_all_matchs, date=today),
            width=UserInterface.BUTTONS_WIDTH)
        self.get_todays_matchs_button.grid(row=4, column=0)

        self.get_tomorrows_matchs_button = Button(
            text=f"Get Matchs : {(datetime.today() + timedelta(days=1)).strftime('%A %d %B')}",
            command=partial(get_matchs.get_all_matchs, date=tomorrow), width=UserInterface.BUTTONS_WIDTH)
        self.get_tomorrows_matchs_button.grid(row=4, column=1)

        self.get_J2_matchs_button = Button(
            text=f"Get Matchs : {(datetime.today() + timedelta(days=2)).strftime('%A %d %B')}",
            command=partial(get_matchs.get_all_matchs, date=j2), width=UserInterface.BUTTONS_WIDTH)
        self.get_J2_matchs_button.grid(row=4, column=2)

        self.get_J3_matchs_button = Button(
            text=f"Get Matchs : {(datetime.today() + timedelta(days=3)).strftime('%A %d %B')}",
            command=partial(get_matchs.get_all_matchs, date=j3), width=UserInterface.BUTTONS_WIDTH)
        self.get_J3_matchs_button.grid(row=4, column=3)

        self.get_J4_matchs_button = Button(
            text=f"Get Matchs : {(datetime.today() + timedelta(days=4)).strftime('%A %d %B')}",
            command=partial(get_matchs.get_all_matchs, date=j4), width=UserInterface.BUTTONS_WIDTH)
        self.get_J4_matchs_button.grid(row=4, column=4)

        # Bottom Buttons VIEW
        self.view_todays_matchs_button = Button(
            text=f"View Matchs : {datetime.today().strftime('%A %d %B')}",
            command=partial(self.read_match_list, date=today),
            width=UserInterface.BUTTONS_WIDTH)
        self.view_todays_matchs_button.grid(row=5, column=0)

        self.view_tomorrows_matchs_button = Button(
            text=f"View Matchs : {(datetime.today() + timedelta(days=1)).strftime('%A %d %B')}",
            command=partial(self.read_match_list, date=tomorrow),
            width=UserInterface.BUTTONS_WIDTH)
        self.view_tomorrows_matchs_button.grid(row=5, column=1)

        self.view_tomorrows_matchs_button = Button(
            text=f"View Matchs : {(datetime.today() + timedelta(days=2)).strftime('%A %d %B')}",
            command=partial(self.read_match_list, date=j2),
            width=UserInterface.BUTTONS_WIDTH)
        self.view_tomorrows_matchs_button.grid(row=5, column=2)

        self.view_tomorrows_matchs_button = Button(
            text=f"View Matchs : {(datetime.today() + timedelta(days=3)).strftime('%A %d %B')}",
            command=partial(self.read_match_list, date=j3),
            width=UserInterface.BUTTONS_WIDTH)
        self.view_tomorrows_matchs_button.grid(row=5, column=3)

        self.view_tomorrows_matchs_button = Button(
            text=f"View Matchs : {(datetime.today() + timedelta(days=4)).strftime('%A %d %B')}",
            command=partial(self.read_match_list, date=j4),
            width=UserInterface.BUTTONS_WIDTH)
        self.view_tomorrows_matchs_button.grid(row=5, column=4)

        # Text
        self.textbox = Text(master=self.window)
        self.textbox.grid(row=1, rowspan=3, column=1, columnspan=3)
        self.window.mainloop()

    def read_match_list(self, date):
        self.textbox.delete('1.0', END)
        try:
            with open(f"./Liste de Matchs/{date}.json", "r") as f:
                matchs_list = json.load(f)
        except FileNotFoundError:
            self.textbox.insert(index=1.0, chars="Please get matchs list first")
        else:
            for championship in matchs_list:
                matchs = matchs_list[championship]
                for match in matchs:
                    match_split = match.split("|")
                    home_team = match_split[0]
                    away_team = match_split[1]
                    # show_infos.debug_format_teams(champ=championship, ht=home_team, at=away_team) # Only for Debugging
                    cards_for_stats = show_infos.get_card_for(champ=championship, ht=home_team, at=away_team)
                    cards_against_stats = show_infos.get_card_against(champ=championship, ht=home_team, at=away_team)
                    corners_for_stats = show_infos.get_corner_for(champ=championship, ht=home_team, at=away_team)
                    corners_against_stats = show_infos.get_corner_against(champ=championship, ht=home_team, at=away_team)
                    content = f"Championnat : {championship}" \
                              f"\nMatch : {match.replace('|', ' - ')}" \
                              f"\n{cards_for_stats} Cards For" \
                              f"\n{cards_against_stats} Cards Against" \
                              f"\n{corners_for_stats} Corners For" \
                              f"\n{corners_against_stats} Corners Against\n\n\n"
                    self.textbox.insert(index=1.0, chars=content)
