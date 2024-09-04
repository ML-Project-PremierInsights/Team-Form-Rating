import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
html_content = soup.prettify()
uncommented_html = html_content.replace("<!--", "").replace("-->", "")
soup_uncommented = BeautifulSoup(uncommented_html, "html.parser")
table = soup_uncommented.find("table", {"id": "stats_standard"})
print(table)

offensive_position = {'FW','MF'}
filtered_rows = []
count = 0
for row in table.find('tbody').find_all('tr'):
    if "thead" in row.get("class", []):
        continue
    else:
        count += 1
        filtered_rows.append(row)
print(count)