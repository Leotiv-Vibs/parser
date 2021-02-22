import csv

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_="pagination-pages").find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    adds = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in adds:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''
        try:
            metro = ad.find('div', class_='data').find_all('div', class_='item-address')[-1].text.strip()
        except:
            metro = ''
    a = [title, url, price, metro]
    return a


def main():
    # https://www.avito.ru/rostov-na-donu/telefony/samsung?p=5&q=samsung
    base_url = 'https://www.avito.ru/rostov-na-donu/telefony/samsung?'
    page_part = 'p='
    query_part = '&q=samsung'
    f = open('AVITO.txt', 'w')
    total_pages = get_total_pages(get_html('https://www.avito.ru/rostov-na-donu/telefony/samsung?p=5&q=samsung'))
    for i in range(1, 28):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        print(get_page_data(html))


if __name__ == '__main__':
    main()
# print(get_page_data(get_html('https://www.avito.ru/rostov-na-donu/telefony/samsung?p=5&q=samsung')))
# print(get_html('https://www.avito.ru/rostov-na-donu/telefony/samsung?p=5&q=samsung'))
# print(get_total_pages(get_html('https://www.avito.ru/rostov-na-donu/telefony/samsung?p=5&q=samsung')))
