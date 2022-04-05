#! /usr/bin/python3
from logging import raiseExceptions
import sys
from bs4 import BeautifulSoup
from time import sleep
import requests

def main():
    sleep(5)
    if (len(sys.argv) != 3):
        print("Argv error")
        exit(1)
    ticker = sys.argv[1]
    field = sys.argv[2]
    
    url = "https://finance.yahoo.com/quote/{}/financials".format(ticker)
    response = requests.get(url, headers={'User-Agent': 'PYTHON'})

    soup = BeautifulSoup(response.text, 'lxml')
    result = soup.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    list_element = []
    for element in result:
        if (element.find(text=field) != None):
            list_element.append(field)
            name_column = element.find('div', class_='D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined')
            [list_element.append(i) for i in element.get_text(separator=' ').replace(field, '').strip().split(' ')]
            break
    if (len(list_element) == 0):
        raise Exception()
    print(list_element)
    return (tuple(list_element))

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("ERROR with fields or ticker")