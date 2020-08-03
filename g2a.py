import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.g2a.com',
        'Referer': 'https://www.g2a.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    }
    r = req.get(f'https://www.g2a.com/search?query={query}', headers=headers)
    soup = bs(r.text, "html.parser")

    output = []
    
    for x in soup.find_all('div', { 'class': 'Card__base' }):
        price = x.find('span', { 'class': 'Card__price-cost price' }).text
        title = x.find('h3', { 'class': 'Card__title' }).find("a").text
        data = (title, price, 'g2a')
        print(data)

        output.append(data)
        if len(output) == max:
            return output
    return output
