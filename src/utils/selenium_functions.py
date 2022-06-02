from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def open_browser():
    try:
        service = Service(executable_path=ChromeDriverManager().install())
    except:
        service = Service(executable_path="./chromedriver/chromedriver.exe")
    finally:
        driver = webdriver.Chrome(service=service)
    return driver


def accept_cookie(driver):
    try:
        driver.implicitly_wait(1)
        frame = driver.find_element(By.XPATH, '//*[@id="appconsent"]/iframe')
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[1]/button/span').click()
        driver.switch_to.default_content()
    except NoSuchElementException:
        pass
    finally:
        pass
