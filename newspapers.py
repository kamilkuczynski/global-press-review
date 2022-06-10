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
dw_germany_data = requests.get("https://www.dw.com/en/germany/s-1432")
# print(fox_data)

soup = bs4.BeautifulSoup(raw_data.text, 'lxml')
fox_soup = bs4.BeautifulSoup(fox_data.text, 'lxml')
dw_german_soup = bs4.BeautifulSoup(dw_germany_data.text, 'lxml')
# print(fox_soup.text)


titles = soup.select('.article-trending.u-clickable-card')
fox_titles = fox_soup.select('.title > a')
dw_titles = dw_german_soup.select('.news')
# pprint.pprint(dw_titles)

list_of_titles = []
'''
print("Al jazeera")
for title in titles[0:5]:
    list_of_titles.append(title.text)
pprint.pprint(list_of_titles[0:7])

print()
print("Fox News")
for title in fox_titles[1:11]:
    list_of_titles.append(title.text.replace("\n",""))
pprint.pprint(list_of_titles[7:12])
'''

print()
german_titles = []
print("Deutsche Welle - Germany")
for title in dw_titles[1:6]:
    print(title.select('h2')[0].text, "\n", "https://www.dw.com"+title.select('a')[0]['href'])

    # german_titles.append(title.text.replace("\n" ,""))
pprint.pprint(german_titles)

# pprint.pprint(list_of_titles)