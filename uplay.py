import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    r = req.get(f'https://store.ubi.com/at/search?q={query}', headers=headers)
    soup = bs(r.text, "html.parser")
    output = []
    
    results = soup.find('div', { 'id': 'card-details-wrapper '})

    for x in results.findChildren('a', recusive=False):
        price = float(x.find('div', {'class': 'product-price price deal discount-shown ' }).text
        title = x.find('h2', { 'class': 'prod-title' }).text

        data = (title, price, 'steam')
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