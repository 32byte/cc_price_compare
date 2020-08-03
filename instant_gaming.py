import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    r = req.get(f'https://www.instant-gaming.com/en/search/?q={query}')
    soup = bs(r.text, "html.parser")

    output = []
    
    for x in soup.find_all('div', { 'class': 'category-best item mainshadow' }):
        price = x['data-price']
        title = x.find('div', { 'class': 'name' }).text
        if not dlc:
            if x['data-dlc'] == '0':
                output.append((title, price))    
        else:
            if x['data-dlc'] == '1':
                output.append((title, price))
        if len(output) == max:
            return output
    return output