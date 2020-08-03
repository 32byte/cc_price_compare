import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    r = req.get(f'https://www.g2a.com/search?query={query}')
    soup = bs(r.text, "html.parser")

    output = []
    
    for x in soup.find_all('div', { 'class': 'products-grid__item' }):
        price = x.find('span', { 'class': 'Card__price-cost price' }).text
        title = x.find('h3', { 'class': 'Card__title' }).find("a").text
        data = (title, price, 'g2a')
        print(data)

        output.append(data)
        if len(output) == max:
            return output
    return output

get_prices("gta")
