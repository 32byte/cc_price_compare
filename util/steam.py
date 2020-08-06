import requests as req
from bs4 import BeautifulSoup as bs

def get_prices(query, dlc=False, max=3):
    headers = {
        'Host': 'store.steampowered.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://store.steampowered.com/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    r = req.get(f'https://store.steampowered.com/search/?term={query}', headers=headers)
    soup = bs(r.text, "html.parser")
    output = []
    
    results = soup.find('div', { 'id': 'search_resultsRows'})

    for x in results.findChildren('a', recusive=False):
        price = float(x.find('div', {'class': 'col search_price_discount_combined responsive_secondrow' })['data-price-final']) / 100
        title = x.find('span', { 'class': 'title' }).text

        data = (title, price, 'steam')
        
        if not dlc:
            if 'dlc' in title.lower():
                pass
            elif "expansion pack" in title.lower():
                pass
            elif "season pass" in title.lower():
                pass
            elif price <= 0:
                pass
            else:
                output.append(data)
        else:
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