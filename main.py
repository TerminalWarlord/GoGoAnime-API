# Copyright © 2021 TerminalWarlord
# Encoding = 'utf-8'
# Licensed under MIT License
# https://github.com/TerminalWarlord/


import requests
from bs4 import BeautifulSoup as bs


def latestepisodes():
    r = requests.get('https://ajax.gogo-load.com/ajax/page-recent-release.html?page=1&type=1')
    soup = bs(r.text, "html.parser")
    animes = soup.find("ul", {"class": "items"}).find_all("li")
    animesjson = []
    for anime in animes:
        item = {
            'title' : anime.find("p", {"class": "name"}).find("a").text.strip() + " " + anime.find("p", {"class": "episode"}).text.strip(),
            'image' : anime.find("div", {"class": "img"}).find("img").attrs['src'],
            'url' : "https://gogoanime.pe" + anime.find("div", {"class": "img"}).find("a").attrs['href']
        }
        animesjson.append(item)
    s = requests.get('https://ajax.gogo-load.com/ajax/page-recent-release.html?page=1&type=2')
    soup = bs(s.text, "html.parser")
    animes = soup.find("ul", {"class": "items"}).find_all("li")
    for anime in animes:
        item = {
            'title' : anime.find("p", {"class": "name"}).find("a").text.strip() + " " + anime.find("p", {"class": "episode"}).text.strip(),
            'image' : anime.find("div", {"class": "img"}).find("img").attrs['src'],
            'url' : "https://gogoanime.pe" + anime.find("div", {"class": "img"}).find("a").attrs['href']
        }
        animesjson.append(item)
    t = requests.get('https://ajax.gogo-load.com/ajax/page-recent-release.html?page=1&type=3')
    soup = bs(t.text, "html.parser")
    animes = soup.find("ul", {"class": "items"}).find_all("li")
    for anime in animes:
        item = {
            'title' : anime.find("p", {"class": "name"}).find("a").text.strip() + " " + anime.find("p", {"class": "episode"}).text.strip(),
            'image' : anime.find("div", {"class": "img"}).find("img").attrs['src'],
            'url' : "https://gogoanime.pe" + anime.find("div", {"class": "img"}).find("a").attrs['href']
        }
        animesjson.append(item)
    return animesjson
