import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from constant import LIST_CHAMPIONSHIP, CONVERSION_LIST
import os

all_matchs = {}


def open_browser():
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except:
        service = Service(executable_path="./chromedriver/chromedriver.exe")
    finally:
        opt = Options()
        opt.add_argument("Chrome/100.0.4896.127")
        driver = webdriver.Chrome(service=service, options=opt)
    return driver


def get_href_results():
    url = "https://www.matchendirect.fr/resultat-foot-08-05-2022/"

    driver = open_browser()
    driver.get(url)
    driver.implicitly_wait(5)

    frame = driver.find_element(By.XPATH, '//*[@id="appconsent"]/iframe')
    driver.switch_to.frame(frame)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/aside/section/button[2]').click()


if __name__ == "__main__":
    get_href_results()