#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pymysql
from bs4 import BeautifulSoup

BEAN_TOP_250_URL = 'https://movie.douban.com/top250'
SUFFIX = '人评价'


def download_page(url):
    print("download_page url=", url)
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    data = requests.get(url, headers=head).content
    return data
    #  return data


##  [<span class="title">肖申克的救赎</span>, <span class="title"> / The Shawshank Redemption</span>]
## find 获取的是<span class="title">肖申克的救赎</span>
## find_all 获取的是list [XXX,RRR,HHH]
def parse_html_bean_top_250(html):
    print("parse_html html=", html)
    soup = BeautifulSoup(html)
    movie_list = soup.find('ol', attrs={'class': 'grid_view'})
    li_list = movie_list.find_all('li')
    for li in li_list:
        a_href = li.find('div', attrs={'class': 'pic'})
        ## a标签.get('href') 或者 a标签['href'] 都可以获取链接数据
        href = a_href.find('a')['href']
        img = a_href.find('img').get('src')
        print("href=", href)
        print("img=", img)
        detail = li.find('div', attrs={'class': 'hd'})
        title = detail.find('span', attrs={'class': 'title'}).getText()
        print("title=", title)
        peoples = li.find('div', attrs={'class': 'bd'})
        director = peoples.find('p').get_text()
        print("director=", director)
        scorediv = li.find('div', attrs={'class': 'star'})
        score = scorediv.find('span', attrs={'class': 'rating_num'}).getText()
        print("score=", score)
        numbers = scorediv.find_all('span')[3].getText()
        print("numbers=", numbers.replace(SUFFIX, ''))
        quote = li.find('p', attrs={'class': 'quote'}).getText()
        print("quote=", quote)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    print('next_page=', next_page)

    if (next_page):
        return BEAN_TOP_250_URL + next_page['href']
    return None
    # return find


# print("download_page result=", download_page(BEAN_TOP_250_URL))
# print("parse_html result=", parse_html(download_page(BEAN_TOP_250_URL)))

def main():
    url = BEAN_TOP_250_URL
    while url:
        page = download_page(url)
        url = parse_html_bean_top_250(page)


if __name__ == '__main__':
    main()
