#!usr/bin/env python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import arrow


def get_todays_games():
    """
    :rtype: [{}]
    :params:
        bbc livescore url
    :return:
        list of dictionaries for todays games
        [{'home': 'Uruguay', 'away': 'Saudi Arabia'}, {'home': 'Portugal', 'away': 'Morocco'}, {'home': 'Iran', 'away': 'Spain'}, {'home': 'Honka', 'away': 'SJK'}, {'home': 'Ilves', 'away': 'Lahti'}, {'home': 'KuPS Kuopio', 'away': 'HJK Helsinki'}, {'home': 'TPS Turku', 'away': 'Inter Turku'}, {'home': 'VPS Vaasa', 'away': 'IFK Mariehamn'}]
    """

    my_url = 'https://www.bbc.co.uk/sport/football/scores-fixtures/{}'.format(arrow.now().format('YYYY-MM-DD'))

    u_client = uReq(my_url)
    # time.sleep(10)
    page_html = u_client.read()
    u_client.close()
    page_soup = soup(page_html, "html.parser")

    li = page_soup.findAll("li", {"class": "gs-u-pb-"})

    matches_list = []
    for match in li:
        col = match.findAll("span", {"class": "gs-u-display-none"})
        matchDict = {"home": col[0].text, "away": col[1].text}
        matches_list.append(matchDict)

    return matches_list