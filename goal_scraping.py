import requests
from bs4 import BeautifulSoup

season_start = 2000


while (season_start <= 2023):
    url = f'https://fbref.com/en/comps/9/{season_start}-{season_start+1}/keepers/{season_start}-{season_start+1}-Premier-League-Stats'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    html_content = soup.prettify()
    uncommented_html = html_content.replace("<!--", "").replace("-->", "")
    soup_uncommented = BeautifulSoup(uncommented_html, "html.parser")
    table = soup_uncommented.find("table", {"id": "stats_keeper"})
    # print(table)

    # offensive_position = {'DF','MF'}
    filtered_rows = []
    count = 0

    output = ""

    headers = "Name,Pos,Squad,Macthes Played,Goals Against, Shots on Target Against, Saves, Saves%,W,D,L,Clean Sheets, CS%\n"
    output += headers

    team_stat_data = []

    for row in table.find('tbody').find_all('tr'):
        if "thead" in row.get("class", []):
            continue
        else:
            count += 1
            filtered_rows.append(row)
            row_data = [td.text.strip() for td in row.find_all('td')]
            filtered_row_data = [row_data[0], row_data[2], row_data[3],row_data[6], row_data[10], row_data[12], row_data[13], row_data[14], row_data[15], row_data[16], row_data[17], row_data[18], row_data[19]]
            output += ",".join(filtered_row_data) + "\n"


    # print(count)
    # print(team_stat_data)
    # print(len(team_stat_data))

    # team_set = {team[2] for team in team_stat_data}
    # # print(team_set)
    # team_set_dict = {team: [] for team in team_set}
    # for team in team_stat_data:
    #     temp_team = team.copy()
    #     team_set_dict[team[2]].append(team)

    # print(team_set_dict['Manchester City'])
    # print('\n\n')
    # for team in team_set_dict:
    #     team_set_dict[team].sort(key=lambda x: int(x[3]), reverse=True)
    # print(team_set_dict['Manchester City'])

    with open(f'keeping_stats/{season_start}-{season_start+1}.csv', 'w', encoding='utf-8') as f:
        f.write(output)
    
    season_start += 1