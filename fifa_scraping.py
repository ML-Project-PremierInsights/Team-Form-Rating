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
driver = webdriver.Chrome(service=service)
driver.get(base_url+suffix_url1+str(1)+suffix_url2)
page_nums = int((driver.find_elements(By.CLASS_NAME, 'pagination'))[-1].text[-2::])
print(page_nums+1)
h1 = driver.find_element(By.CLASS_NAME, 'table-players')
print(h1.text)
temp_list = h1.text.split('\n')[1::]
print('\n\n')
print(temp_list)
print('\n\n')
player_data+=temp_list

# pc = int(driver.find_elements(By.CLASS_NAME, 'page-link')[-1].text)
# print(pc+1)

driver.quit()

# player_data = []
for i in range(2, page_nums+1):
    driver = webdriver.Chrome(service=service)
    driver.get(base_url+suffix_url1+str(i)+suffix_url2)
    h1 = driver.find_element(By.CLASS_NAME, 'table-players')
    print(h1.text)
    temp_list = h1.text.split('\n')[1::]
    print('\n\n')
    print(temp_list)
    print('\n\n')
    player_data+=temp_list
    driver.quit()

print(player_data)
print('\n\n')
p_data = []
count = 0
for i in player_data:
    yl = i.split(' ')
    ovr = yl[0]  
    pos = yl[-2]  
    age = yl[-1]  
    name = ''.join(yl[1:-2]).lower() 

    # Append the processed data
    p_data.append([ovr, name, pos, age])

# print(p_data)
print('\n\n')

df = pd.DataFrame(p_data, columns=['OVR', 'Name', 'Pos', 'Age'])
print(df)
print('\n\n')

#df.to_csv('fifa_rating_23.csv', index=False)
print(count)
