import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query):
    r = req.get(f'https://www.instant-gaming.com/en/search/?q={query}')
    soup = bs(r.text)

    print(soup)