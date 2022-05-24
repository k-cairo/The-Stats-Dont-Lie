from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from utils.selenium_functions import open_browser
from blog.models import TeamIframe, MatchsTermine


class Command(BaseCommand):
    help = 'Update Historique Matchs'

    def handle(self, *args, **options):
        all_teams_query = TeamIframe.objects.all()

        for query in all_teams_query:
            driver = open_browser()
            driver.get(url=query.iframe_url)

            trs = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

            for tr in trs[3:-2]:
                tds = tr.find_elements(By.CSS_SELECTOR, "td")
                date = tds[1].text
                ht = tds[2].text
                ht_score = tds[3].text
                at_score = tds[4].text
                at = tds[5].text
                corner_for = tds[13].text
                corner_against = tds[14].text
                yellow_card_for = tds[16].text
                yellow_card_against = tds[17].text
                red_card_for = tds[18].text
                red_card_against = tds[19].text
                datas = (
                    date, ht, ht_score, at_score, at, corner_for, corner_against, yellow_card_for, yellow_card_against,
                    red_card_for, red_card_against)

                if len(MatchsTermine.objects.filter(target_team=query.team).filter(date=date)) == 0 and all(
                        data != "" for data in datas):
                    MatchsTermine.objects.create(target_team=query.team,
                                                 date=date,
                                                 home_team=ht,
                                                 score=f"{ht_score} - {at_score}",
                                                 away_team=at,
                                                 corner_for=corner_for,
                                                 corner_against=corner_against,
                                                 yellow_card_for=yellow_card_for,
                                                 yellow_card_against=yellow_card_against,
                                                 red_card_for=red_card_for,
                                                 red_card_against=red_card_against)

        self.stdout.write('Historique Matchs Updated Successfully')
