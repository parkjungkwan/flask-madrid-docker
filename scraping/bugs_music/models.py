from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""


class Bugmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        _ = 0
        artists = soup.find_all(name='p', attrs={'class':'artist'})
        titles = soup.find_all(name='p', attrs={'class':'title'})
        print(f'List size is {len(artists)}')
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist : {i.find('a').text},  Title : {j.find('a').text}" )


class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers= self.headers)
        soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'lxml')
        _ = 0
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        print(f'List size is {len(artists)}')
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist : {i.find('a').text},  Title : {j.find('a').text}")

def main():
    # 20210720
    # 16
    Bugmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                  f'chartdate={"20210720"}&charthour={"16"}').scrap()


if __name__ == '__main__':
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072016').scrap()


from bs4 import BeautifulSoup
import pandas as pd
import requests



class MusicRanking(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    tag_name = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'Crawling HTML is {self.html}')
    def get_raking(self):
        soup = BeautifulSoup(self.html, 'lxml')

    def insert_dict(self):
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        # 방법 3
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]

        print(dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')





