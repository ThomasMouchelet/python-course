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

driver.get("https://www.amazon.fr")


try:
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys('iphone 14')
    search_box.send_keys(Keys.ENTER)

    prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

    for price in prices:
        print(price.text)
except Exception as e:
    assert False, "search_box not found"