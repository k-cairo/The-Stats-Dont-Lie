from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from utils.selenium_functions import open_browser
from blog.models import TeamIframe, MatchsTermine


def create_histo_match_in_database(query, datas):
    if len(MatchsTermine.objects.filter(target_team=query.team).filter(date=datas[0])) == 0 and all(
            data != "" for data in datas):
        return MatchsTermine.objects.create(target_team=query.team, date=datas[0], home_team=datas[1],
                                            score=f"{datas[2]} - {datas[3]}", away_team=datas[4], corner_for=datas[5],
                                            corner_against=datas[6], yellow_card_for=datas[7],
                                            yellow_card_against=datas[8], red_card_for=datas[9],
                                            red_card_against=datas[10])


def get_all_stats(tr):
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
    return (date, ht, ht_score, at_score, at, corner_for, corner_against, yellow_card_for, yellow_card_against,
            red_card_for, red_card_against)


class Command(BaseCommand):
    help = 'Update Historique Matchs'

    def handle(self, *args, **options):
        driver = open_browser()
        all_teams_query = TeamIframe.objects.all()

        for query in all_teams_query:
            driver.get(url=query.iframe_url)
            trs = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

            for tr in trs[3:-2]:
                datas = get_all_stats(tr=tr)
                create_histo_match_in_database(query=query, datas=datas)

        self.stdout.write('Historique Matchs Updated Successfully')
