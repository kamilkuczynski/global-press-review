#TODO 1: dodać linki
#TODO 2: dodać foxnews, dw.de, russian Today, France24, any Chinese
#TODO 3: dodać zapis do txt
#TODO 4: zrobić gui w tkinker
#TODO 5:

import pprint
import bs4
import requests

raw_data = requests.get("https://www.aljazeera.com/")
fox_data = requests.get("https://www.foxnews.com/")
dw_germany_data = requests.get("https://www.dw.com/en/germany/s-1432")
russian_today_data = requests.get("https://www.rt.com/")
scmp_data = requests.get('https://www.scmp.com/rss/318198/feed')
# print(fox_data)

soup = bs4.BeautifulSoup(raw_data.text, 'lxml')
fox_soup = bs4.BeautifulSoup(fox_data.text, 'lxml')
dw_german_soup = bs4.BeautifulSoup(dw_germany_data.text, 'lxml')
russian_soup = bs4.BeautifulSoup(russian_today_data.text, 'lxml')
scmp_soup = bs4.BeautifulSoup(scmp_data.text, 'lxml')
# pprint.pprint(scmp_soup)


titles = soup.select('.article-trending.u-clickable-card')
fox_titles = fox_soup.select('.title > a')
dw_titles = dw_german_soup.select('.news')
russian_titles = russian_soup.select('.card')
scmp_titles = scmp_soup.select('item')
# pprint.pprint(scmp_titles)

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


print()
german_titles = []
print("Deutsche Welle - Germany")
for title in dw_titles[1:6]:
    print(title.select('h2')[0].text, "\n", "https://www.dw.com"+title.select('a')[0]['href'])

    # german_titles.append(title.text.replace("\n" ,""))
pprint.pprint(german_titles)

print("Russian Today - Russia")
russian_list_titles = []
for title in russian_titles:
    russian_list_titles.append(title.text)
    # print(title.text.)

pprint.pprint(russian_list_titles)
'''
#
print()
# print("Politics - South China Morning Post")
for title in scmp_soup.select("item")[1:5]:
    pprint.pprint(title.select('title')[0].text)
    pprint.pprint(title.select('link')[0].text)
    pprint.pprint(title.select('description')[0].text)
    print()
    # list_of_titles.append(title.text.replace("\n",""))
# pprint.pprint(list_of_titles[7:12])
# pprint.pprint(scmp_soup.select('title'))
# pprint.pprint(scmp_soup.select('link'))