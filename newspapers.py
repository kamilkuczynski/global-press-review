# TODO 1: dodać linki
# TODO 2: dodać foxnews, dw.de, russian Today, France24, any Chinese
# TODO 3: dodać zapis do txt
# TODO 4: zrobić gui w tkinker


import bs4
import requests
from datetime import datetime

raw_data = requests.get("https://www.aljazeera.com/")
fox_data = requests.get("https://www.foxnews.com/")
dw_germany_data = requests.get("https://www.dw.com/")
scmp_data = requests.get('https://www.scmp.com/news/china?module=mega_menu_news_int&pgtype=homepage')
print(scmp_data)

soup = bs4.BeautifulSoup(raw_data.text, 'lxml')
fox_soup = bs4.BeautifulSoup(fox_data.text, 'lxml')
dw_german_soup = bs4.BeautifulSoup(dw_germany_data.text, 'lxml')
scmp_soup = bs4.BeautifulSoup(scmp_data.text, 'html.parser')


titles = soup.select('.article-trending__content')
fox_titles = fox_soup.select('.title > a')
dw_titles = dw_german_soup.select('.news')
scmp_titles = scmp_soup.select('.article__title')
# pprint.pprint(scmp_titles)

list_of_titles = []


print("===== Al jazeera =====")
list_of_titles.append("===== Al jazeera =====")

for title in titles[0:5]:
    print(title.text)
    print("https://www.aljazeera.com/" + title.a['href'] + "\n")
    list_of_titles.append(title.text + "\n"
                          "https://www.aljazeera.com/" + title.a['href'] + "\n")


print()
print("===== Fox News =====")
list_of_titles.append("===== Fox News =====")

for title in fox_titles[1:5]:
    print(title.text)
    print(title['href'] + "\n")
    list_of_titles.append(title.text.replace("\n", "") + "\n" +
                          title['href'] + "\n")


print()
german_titles = []
print("=====Deutsche Welle - Germany=====")
list_of_titles.append("=====Deutsche Welle - Germany=====")

for title in dw_titles[1:6]:
    print(title.select('h2')[0].text.strip())
    print("https://www.dw.com" + title.select('a')[0]['href'] + "\n")
    list_of_titles.append(title.select('h2')[0].text.strip() + "\n" +
                          "https://www.dw.com" + title.select('a')[0]['href'] + "\n")


print()
print("=====Politics - South China Morning Post=====")
list_of_titles.append("=====Politics - South China Morning Post=====")

for title in scmp_titles[1:6]:
    print(title.text.strip())
    print(" https://www.scmp.com" + title.select("a")[0]['href']+ "\n")
    #We can left an empty line by function print()

    list_of_titles.append(title.text.splitlines()[0] +
                          "\nhttps://www.scmp.com" + title.select("a")[0]['href'])
# pprint.pprint(list_of_titles[7:12])


# SAVE a data to a file

date = datetime.today().strftime("%Y_%m_%d")

try:
    file =  open(date + '_daily_word_news_review.txt', 'w')
    for items in list_of_titles:
        file.writelines([items + '\n' + '\n'])
except FileNotFoundError as error_message:
    print("There was an error: ", error_message)
finally:
    file.close()
    print("File was closed")
