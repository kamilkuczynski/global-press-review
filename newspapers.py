# TODO 1: dodać linki
# TODO 2: dodać foxnews, dw.de, russian Today, France24, any Chinese
# TODO 3: dodać zapis do txt
# TODO 4: zrobić gui w tkinker

from datetime import datetime
import bs4
import config
import requests
import smtplib

def fetch_soup(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text, 'html.parser')

def fetch_aljazeera_titles():
    soup = fetch_soup('https://www.aljazeera.com/')
    titles = soup.select('.article-trending__content')
    return [(title.text, 'https://www.aljazeera.com' + title.a['href']) for title in titles[0:5]]

def fetch_foxnews_titles():
    soup = fetch_soup('https://www.foxnews.com/')
    fox_titles = soup.select('.title > a')
    return [(title.text.replace("\n", ""), title['href']) for title in fox_titles[1:5]]

def fetch_scmp_titles():
    soup = fetch_soup('https://www.scmp.com/news/china')
    titles = soup.find_all('h2', class_='article__title')
    seen_titles = set()
    result = []
    for title in titles[1:8]:
        link = title.find('a')['href']
        title_text = title.get_text().strip()
        if title_text not in seen_titles:
            result.append((title_text, f'https://www.scmp.com{link}'))
            seen_titles.add(title_text)
    return result

def save_to_file(data):
    date = datetime.today().strftime("%Y_%m_%d")
    filename = f'{date}_daily_word_news_review.txt'
    with open(filename, 'w') as file:
        for title, url in data:
            file.write(f'{title}\n{url}\n\n')
    print(f'Data saved to file {filename}')

def main():
    aljazeera_titles = fetch_aljazeera_titles()
    foxnews_titles = fetch_foxnews_titles()
    scmp_titles = fetch_scmp_titles()

    print("===== Al jazeera =====")
    for title, url in aljazeera_titles:
        print(f'{title}\n{url}\n')
    print("===== Fox News =====")
    for title, url in foxnews_titles:
        print(f'{title}\n{url}\n')
    print("===== Politics - South China Morning Post =====")
    for title, url in scmp_titles:
        print(f'{title}\n{url}\n')

    data = aljazeera_titles + foxnews_titles + scmp_titles
    save_to_file(data)

if __name__ == '__main__':
    main()

# Send titles and links by email:
email = "kamil.kuczynski4@gmail.com"

try:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=config.gmail_password)
        connection.sendmail(from_addr=email,
                            to_addrs="kamil.kuczynski4@gmail.com",
                            msg=f"Subject:News from the World.\n\n "
                                f"{list_of_titles}"
                                f"\n Have a nice day".encode("utf-8"))

except UnicodeEncodeError:
    print("UnicodeEncodeError :(")
