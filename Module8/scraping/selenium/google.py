from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

# Chargez les variables d'environnement du fichier .env
load_dotenv()

GOOGLE_ACCOUNT_MAIL = os.getenv('GOOGLE_ACCOUNT_MAIL')
GOOGLE_ACCOUNT_PASSWORD = os.getenv('GOOGLE_ACCOUNT_PASSWORD')

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get("https://google.com")

# select button id gksS1d
driver.find_element(By.ID, "gksS1d").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys(GOOGLE_ACCOUNT_MAIL)
time.sleep(2)
driver.find_element(By.ID, "identifierNext").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(GOOGLE_ACCOUNT_PASSWORD)
time.sleep(2)
driver.find_element(By.ID, "passwordNext").click()