from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

service = Service('C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')


base_url = 'https://www.fifaindex.com/players/fifa23_589/'
suffix_url1 = '?page='
suffix_url2 = '&gender=0&league=13&order=desc'


player_data = []
for i in range(1,5):
    driver = webdriver.Chrome(service=service)
    driver.get(base_url+suffix_url1+str(i)+suffix_url2)
    #wait = WebDriverWait(driver, 3)
    #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a.sc-2vbwj7-22.blyzsR")))
    h1 = driver.find_element(By.CLASS_NAME, 'table-players')
    print(h1.text)
    driver.quit()


