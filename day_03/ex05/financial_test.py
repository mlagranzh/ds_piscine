#! /usr/bin/python3
from logging import raiseExceptions
import sys
from bs4 import BeautifulSoup
from time import sleep
import requests
import pytest


def test_field_for_ticker():
    test_field = 'Total Revenue'
    test_ticker = 'msft'
    result = main(('dsfsdd', test_ticker, test_field))
    assert result[0] == test_field

def test_ticker_error():
    test_field = 'Tdotal Revenue'
    test_ticker = 'msft'
    with pytest.raises(Exception, match=f"Ticker ERROR'"):
        main(('dsfsdd',test_ticker,test_field))

def test_type():
    test_field = 'Total Revenue'
    test_ticker = 'msft'
    assert isinstance(main(('dsfsdd',test_ticker,test_field)), tuple)

def main(argv=sys.argv):
    sleep(5)
    if (len(argv) != 3):
        print("Argv error")
        exit(1)
    ticker = argv[1]
    field = argv[2]
    
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
    
    try:
        test_field_for_ticker()
    except AssertionError:
        print("ERROR with ticker")

#python3 -m pytest financial_test.py