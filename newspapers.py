#TODO 1: dodać linki
#TODO 2: dodać foxnews
#TODO 3: dodać zapis do txt
#TODO 4: zrobić gui w tkinker
#TODO 5:

import pprint

import bs4
import requests

raw_data = requests.get("https://www.aljazeera.com/")

soup = bs4.BeautifulSoup(raw_data.text, 'lxml')
titles = soup.select('.article-trending.u-clickable-card')
# print(titles)

list_of_titles = []

for title in titles:
    list_of_titles.append(title.text)

pprint.pprint(list_of_titles)
