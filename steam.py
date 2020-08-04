import requests as req
from bs4 import BeautifulSoup as bs

def idiot_cyka(query, dlc=False, max=3):
    r = req.get(f'https://store.steampowered.com/search/?term={query}')
    soup = bs(r.text, "html.parser")

    output = []
    
    for x in soup.find_all('a', { 'class': 'search_result_row ds_collapse_flag  app_impression_tracked' }):
        price = x.find('div', {'class': 'col search_price  responsive_secondrow' }).text
        title = x.find('span', { 'class': 'title' }).text
        data = (title, price, 'steam')
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
    idiot_cyka(game)
    
if __name__ == "__main__":
    main()