import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    r = req.get(f'https://www.instant-gaming.com/en/search/?q={query}')
    soup = bs(r.text, "html.parser")

    output = []
    
    for x in soup.find_all('div', { 'class': 'category-best item mainshadow' }):
        price = x['data-price']
        title = x.find('div', { 'class': 'name' }).text
        data = (title, price, 'instant-gaming')
        if not dlc:
            if x['data-dlc'] == '0':
                output.append(data)
        else:
            if x['data-dlc'] == '1':
                output.append(data)
        if len(output) == max:
            return output
    return output


def main():
    game = input("Game to compare: ")
    get_prices(game)

if __name__ == "__main__":
    main()