import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    r = req.get(f'https://www.instant-gaming.com/en/search/?type%5B%5D=steam&type%5B%5D=origin&type%5B%5D=uplay&type%5B%5D=battle.net&type%5B%5D=rockstar&all_cats=1&min_price=0&max_price=100&noprice=1&min_discount=0&max_discount=100&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&available_in=AT&gametype=all&sort_by=&query={query}', timeout=5)
    soup = bs(r.text, "html.parser")

    output = []
    
    for x in soup.find_all('div', { 'class': 'category-best item mainshadow' }):
        price = x['data-price']

        if 'n/a' in x.find('div', { 'class': 'price' }).text.lower():
            continue

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
