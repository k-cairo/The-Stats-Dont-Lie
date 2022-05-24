from django.core.management.base import BaseCommand
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.constant import today
from utils.selenium_functions import open_browser
from blog.models import Iframe, TeamIframe


class Command(BaseCommand):
    help = 'Update Teams iframes'

    def handle(self, *args, **options):
        all_links = {}
        driver = open_browser()
        querysets = Iframe.objects.filter(iframe_stats="cards against")

        for queryset in querysets:
            driver.get(url=queryset.iframe_url)

            div_tbody = driver.find_element(By.CSS_SELECTOR, "tbody")
            all_tr = div_tbody.find_elements(By.CSS_SELECTOR, "tr")

            for tr in all_tr[2:-1]:
                try:
                    team = tr.find_element(By.CSS_SELECTOR, "td a").text
                except NoSuchElementException:
                    print("Problem")
                else:
                    team_link = tr.find_element(By.CSS_SELECTOR, "td a").get_attribute("href")
                    all_links[team] = team_link

        for team, link in all_links.items():
            driver.get(link)
            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[2]/main/div/section/div/div/div[5]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys(
                    "cairo.kevin72@gmail.com")
                driver.find_element(By.XPATH, '//*[@id="user_pass"]').send_keys("31Mars1988" + Keys.ENTER)
            except NoSuchElementException:
                pass
            finally:
                divs_content = driver.find_elements(By.CSS_SELECTOR, "div.tab-content")
                iframe = divs_content[1].find_element(By.CSS_SELECTOR, "iframe").get_attribute("src")

                if len(TeamIframe.objects.filter(team=team)) == 0:
                    TeamIframe.objects.create(team=team,
                                              iframe_url=iframe,
                                              iframe_stats="histo_overall",
                                              date_updated=today)
                else:
                    TeamIframe.objects.filter(team=team).update(iframe_url=iframe, date_updated=today)

        self.stdout.write('Teams Iframes Updated Successfully')
