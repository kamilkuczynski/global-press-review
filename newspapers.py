# TODO 1: dodać linki
# TODO 2: dodać foxnews, dw.de, russian Today, France24, any Chinese
# TODO 3: dodać zapis do txt
# TODO 4: zrobić gui w tkinker
# TODO 5:

import pprint
import bs4
import requests
import lxml
from datetime import datetime

raw_data = requests.get("https://www.aljazeera.com/")
fox_data = requests.get("https://www.foxnews.com/")
dw_germany_data = requests.get("https://www.dw.com/en/germany/s-1432")
russian_today_data = requests.get("https://www.rt.com/")
scmp_data = requests.get('https://www.scmp.com/news/china?module=mega_menu_news_int&pgtype=homepage')
print(scmp_data)

soup = bs4.BeautifulSoup(raw_data.text, 'lxml')
fox_soup = bs4.BeautifulSoup(fox_data.text, 'lxml')
dw_german_soup = bs4.BeautifulSoup(dw_germany_data.text, 'lxml')
russian_soup = bs4.BeautifulSoup(russian_today_data.text, 'lxml')
scmp_soup = bs4.BeautifulSoup(scmp_data.text, 'html.parser')
# pprint.pprint(scmp_soup)


titles = soup.select('.article-trending.u-clickable-card')
fox_titles = fox_soup.select('.title > a')
dw_titles = dw_german_soup.select('.news')
russian_titles = russian_soup.select('.card')
scmp_titles = scmp_soup.select('.article__title')
# pprint.pprint(scmp_titles)

list_of_titles = []

print("Al jazeera")
for title in titles[0:5]:
    list_of_titles.append(title.text)
pprint.pprint(list_of_titles[0:7])

print()
print("Fox News")
for title in fox_titles[1:11]:
    list_of_titles.append(title.text.replace("\n", ""))
    print(title.text)
# pprint.pprint(list_of_titles[7:12])


print()
german_titles = []

print("Deutsche Welle - Germany")

for title in dw_titles[1:6]:
    print(title.select('h2')[0].text, "\n",
          "https://www.dw.com" + title.select('a')[0]['href'])

    german_titles.append(title.text.replace("\n", ""))
    list_of_titles.append(title.text.replace("\n", ""))

print("Russian Today - Russia")
russian_list_titles = []
for title in russian_titles[:5]:
    # print(title.get_text().splitlines())
    russian_list_titles.append(title.text.strip())
    russian_list_titles.append(title.select('a'))
    list_of_titles.append(title.text.strip())

pprint.pprint(russian_list_titles)

print()
print("Politics - South China Morning Post")

for title in scmp_titles[1:6]:
    pprint.pprint(title.text.splitlines()[0])
    pprint.pprint("https://www.scmp.com" + title.select("a")[0]['href'])
    print()
    list_of_titles.append(title.text.splitlines()[0] +
                          "https://www.scmp.com" + title.select("a")[0]['href'])
# pprint.pprint(list_of_titles[7:12])

# SAVE data to a file


date = datetime.today().strftime("%Y_%m_%d")

with open(date + '_daily_word_news_review.txt', "w") as file:
    for items in list_of_titles:
        file.writelines([items + '\n' + '\n'])
