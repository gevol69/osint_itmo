from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import datetime
import json
from requests.exceptions import ProxyError, ReadTimeout, ConnectTimeout, ConnectionError
import csv
import os

URL = 'https://www.proxyscan.io/'

#собираем валидные прокси на данный момент в csv
def write_csv(dict_data):
    keys = ['ip_address', 'port', 'country_city', 'type_proxy']
    with open('proxy.csv', 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, keys, delimiter=',')
        #проверка на существование файла
        flag_csv_empty = os.stat("proxy.csv").st_size == 0
        if flag_csv_empty:
            writer.writeheader()
        writer.writerows([dict_data])

#получение html странички с прокруткой в selenium
def get_html(url):
    start_loop_global = time.time()
    now = datetime.datetime.now()
    print('Скрипт начал работу... время - {}'.format(now))
    options = Options()
    options.headless = True #без открытия окна браузера
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    end_loop_global = time.time()
    print('Получили страничку за {} c., начинаем парсить и проверять прокси...'.format(round((end_loop_global - start_loop_global), 2)))
    return driver.page_source

#парсим страничку и собираем табличку
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    proxys_table = soup.find('table', attrs={'id':'proxyTable'})
    proxys_table_body = proxys_table.find('tbody')
    rows_proxys_table = proxys_table_body.find_all('tr')
    for row in rows_proxys_table:
        ip_address = row.find('th').text.strip()
        port = row.find_all('td')[0].text.strip()
        country_city = row.find_all('td')[1].text.strip()
        type_proxy = row.find_all('td')[3].text.strip()
        data_proxy = {
            'ip_address' : ip_address,
            'port' : port,
            'country_city' : country_city,
            'type_proxy' : type_proxy
        }
        print('Проверка прокси по адресу {} и порту {} с типом {}....'.format(ip_address, port, type_proxy))
        access_proxy = check_proxy(data_proxy)
        if access_proxy:
            print("\u2713 Прокси {} доступен! Заносим его в файл...".format(ip_address + ':' + port))
            write_csv(data_proxy)
        else:
             print("\u2717 Прокси {} недоступен!".format(ip_address + ':' + port))

        
def check_proxy(data_proxy):
    url = 'https://api.myip.com/'
    if data_proxy['type_proxy'] == 'SOCKS4':
        proxies = {
            'http': 'socks4://{}:{}'.format(data_proxy['ip_address'], data_proxy['port']),
            'https': 'socks4://{}:{}'.format(data_proxy['ip_address'], data_proxy['port'])
        }
    elif data_proxy['type_proxy'] == 'SOCKS5' or data_proxy['type_proxy'] == 'SOCKS5,SOCKS4' or data_proxy['type_proxy'] == 'SOCKS4,SOCKS5':
        proxies = {
            'http': 'socks5://{}:{}'.format(data_proxy['ip_address'], data_proxy['port']),
            'https': 'socks5://{}:{}'.format(data_proxy['ip_address'], data_proxy['port'])
        }
    elif data_proxy['type_proxy'] == 'HTTP':
        proxies = {
            'http': 'http://{}:{}'.format(data_proxy['ip_address'], data_proxy['port']),
            'https': 'http://{}:{}'.format(data_proxy['ip_address'], data_proxy['port'])
        }
        url = 'http://api.myip.com/'
    elif data_proxy['type_proxy'] == 'HTTPS,HTTP' or data_proxy['type_proxy'] == 'HTTP,HTTPS' or data_proxy['type_proxy'] == 'HTTPS':
        proxies = {
            'http': 'https://{}:{}'.format(data_proxy['ip_address'], data_proxy['port']),
            'https': 'https://{}:{}'.format(data_proxy['ip_address'], data_proxy['port'])
        }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
    except ProxyError:
        try:
            response = requests.get(url, proxies=proxies, timeout=5)
        except:
            return False
    except ReadTimeout:
        try:
            response = requests.get(url, proxies=proxies, timeout=5)
        except:
            return False
    except ConnectionError:
        return False
    except ConnectTimeout:
        return False
    if response.status_code == 200:
        try:
            response_dict = json.loads(response.text)
        except:
            return False
        if data_proxy['ip_address'] == response_dict['ip']:
            return True
        else:
            return False


if __name__ == "__main__":
    parse_html(get_html(URL))
