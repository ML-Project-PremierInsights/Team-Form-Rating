import requests
from bs4 import BeautifulSoup
import pandas as pd

pg = 1
main_url = 'https://www.fifaindex.com/players/fifa23_589/?gender=0&league=13&order=desc'

response = requests.get(main_url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())

# table = soup.find('table', {'class': 'table table-striped table-players'})
# rows = table.find('tbody').find_all('tr')
# print(type(table))