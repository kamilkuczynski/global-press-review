#TODO 1: dodać linki
#TODO 2: dodać foxnews
#TODO 3: dodać zapis do txt
#TODO 4: zrobić gui w tkinker
#TODO 5:

import pprint
import bs4
import requests

raw_data = requests.get("https://www.aljazeera.com/")
fox_data = requests.get("https://www.foxnews.com/")
# print(fox_data)

soup = bs4.BeautifulSoup(raw_data.text, 'lxml')
fox_soup = bs4.BeautifulSoup(fox_data.text, 'lxml')
# print(fox_soup.text)


titles = soup.select('.article-trending.u-clickable-card')
fox_titles = fox_soup.select('.title > a')
# pprint.pprint(fox_titles)

list_of_titles = []

for title in titles:
    list_of_titles.append(title.text)

for title in fox_titles[1:11]:
    list_of_titles.append(title.text)

pprint.pprint(list_of_titles)
