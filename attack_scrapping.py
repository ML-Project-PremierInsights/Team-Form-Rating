import requests
from bs4 import BeautifulSoup

url = 'https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
html_content = soup.prettify()
uncommented_html = html_content.replace("<!--", "").replace("-->", "")
soup_uncommented = BeautifulSoup(uncommented_html, "html.parser")
table = soup_uncommented.find("table", {"id": "stats_standard"})

offensive_position = {'FW', 'MF'}
filtered_rows = []
count = 0

output = ""

headers = "Nation,Pos,Squad,Age,Born,MP,Starts,Min,90s,Gls,Ast,G+A,G-PK,PK,PKatt,CrdY,CrdR,xG,npxG,xAG,npxG+xAG,PrgC,PrgP,PrgR,Gls,Ast,G+A,G-PK,G+A-PK,xG,xAG,xG+xAG,npxG,npxG+xAG,Matches\n"
output += headers

for row in table.find('tbody').find_all('tr'):
    if "thead" in row.get("class", []):
        continue
    else:
        count += 1
        filtered_rows.append(row)

        row_data = [td.text.strip() for td in row.find_all('td')]
        output += ",".join(row_data) + "\n" 

print(count)

with open('premier_league_stats.csv', 'w', encoding='utf-8') as f:
    f.write(output)