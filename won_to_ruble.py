import requests
from bs4 import BeautifulSoup


def exchange():
    URL = 'https://finance.rambler.ru/calculators/converter/1-KRW-RUB/'
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")

    price = soup.find_all('div', class_='_20gvL')

    clear_price = []
    for x in price:
        clear_price.append(x.text)

    one_won_to_ruble = clear_price[1]
    one_won_to_ruble = list(one_won_to_ruble)
    one_won_to_ruble = one_won_to_ruble[3:]
    one_won_to_ruble = ''.join(one_won_to_ruble)
    
    return one_won_to_ruble
