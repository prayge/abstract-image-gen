import requests
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pickle
import time

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
url = "https://unsplash.com/s/photos/abstract"
driver.get(url)


def preclick(driver):
    button_class = driver.find_element(By.CLASS_NAME, "gDCZZ")
    button = button_class.find_element(By.TAG_NAME, "button")

    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(button)))
    time.sleep(1)


def get_urls(driver):
    img_div = driver.find_element(
        By.CSS_SELECTOR, "div[data-test='search-photos-route']")
    imgs = img_div.find_elements(By.CLASS_NAME, "YVj9w")

    for e in imgs:
        link = e.get_attribute("src")
        if link not in links:
            print(link)
            links.append(link)


preclick(driver)
links = []

for _ in range(5):
    get_urls(driver)
    for _ in range(6):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1.5)

print(f"lenght of links preset {len(links)}")
links_set = set(links)
links = list(links_set)
print(f"lenght of links after set {len(links)}")

with open('links', 'wb') as f:
    pickle.dump(links, f)
