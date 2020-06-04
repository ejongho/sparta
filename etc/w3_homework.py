import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

genie_raw = BeautifulSoup(data.text, 'html.parser')

musics = list(genie_raw.select('tbody > .list'))
for music in musics:
    rank = music.select_one('td.number')
    title = music.select_one('.info > .title').text.strip()
    artist = music.select_one('.info > .artist').text.strip()
    rank.span.decompose()
    rank = rank.text.strip()
    print(rank,  title,  artist)
    
    
