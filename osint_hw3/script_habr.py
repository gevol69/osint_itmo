import requests
from bs4 import BeautifulSoup
import time
import re

articles = {}
url = 'https://habr.com/ru/all/'

def get_articles():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    article_list = soup.find_all('article', {'class' : 'post post_preview'})
    for article in article_list[::-1]:
        title_article = article.find('h2', {'class' : 'post__title'}).text.strip('\n')
        post_time = article.find('span', {'class' : 'post__time'}).text.strip('\n')
        preview_article = article.find('div', {'class' : 'post__body post__body_crop'}).text.strip('\n').split('\n')[0].strip()
        url_article = article.find('a', {'class' : 'btn btn_x-large btn_outline_blue post__habracut-btn'}).get('href')
        post_stats_views = article.find('span', {'class' : 'post-stats__views-count'}).text.strip('\n')
        article_id = re.search(r'\d+', url_article)[0]
        if article_id not in articles:
            articles[article_id] = {
                    'Title' : title_article,
                    'Time post' : post_time,
                    'Preview' : preview_article,
                    'Url' : url_article,
                    'Views count' : post_stats_views
            }
            print(f'Ура, {post_time} вышла новая статья {article_id}!')
            print(articles[article_id])

while True:
    get_articles()
    print('Следующее обновление через 5 минут!')
    time.sleep(300)
