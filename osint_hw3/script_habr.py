import requests
from bs4 import BeautifulSoup
import time

articles = []
url = 'https://habr.com/ru/all/'

def get_articles(articles):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    article_list = soup.find_all('article', {'class' : 'post post_preview'})
    for artilce in article_list:
        title_article = artilce.find('h2', {'class' : 'post__title'}).text.strip('\n')
        if title_article not in articles:
            articles.append(title_article)

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
article_list = soup.find_all('article', {'class' : 'post post_preview'})
for article in article_list:
    title_article = article.find('h2', {'class' : 'post__title'}).text.strip('\n')
    articles.append(title_article)

while True:
    get_articles(articles)
    print(articles)
    time.sleep(300)