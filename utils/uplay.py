import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    r = req.get(f'https://store.ubi.com/at/search?q={query}', timeout=5)
    soup = bs(r.text, "html.parser")
    output = []

    for x in soup.find_all('div', { 'class': 'product-tile card'}):
        price = float(x.find('span', {'class': 'price-sales standard-price' }).text.replace(',', '.').replace('\n', '').replace('\t', '').replace(' ', '').replace('€', ''))
        title = x.find('h2', { 'class': 'prod-title' }).text.replace(',', '.').replace('\n', '').replace('\t', '').replace('€', '')

        data = (title, price, 'uplay')
        
        if price <= 0:
            pass
        else:
            output.append(data)

        if len(output) == max:
            return output
     
    return output

def main():
    game = input("Game to compare: ")
    get_prices(game)
    
if __name__ == "__main__":
    main()