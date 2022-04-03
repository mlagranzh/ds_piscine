import sys

def ticker_symbols():
    COMPANIES = {
                'Apple': 'AAPL',
                'Microsoft': 'MSFT',
                'Netflix': 'NFLX',
                'Tesla': 'TSLA',
                'Nokia': 'NOK'
                }
    STOCKS = {
                'AAPL': 287.73,
                'MSFT': 173.79,
                'NFLX': 416.90,
                'TSLA': 724.88,
                'NOK': 3.37
                }

    if (len(sys.argv) > 2):
        exit(1)
    for i, param in enumerate(sys.argv):
        if (i != 0):
            try:
                index_company = list(COMPANIES.values()).index(param)
            except ValueError:
                print("Unknown company")
                exit(1)
            company_name = list(COMPANIES.keys())[index_company]
            print(company_name, STOCKS[list(COMPANIES.values())[index_company]])


if __name__ == '__main__':
    ticker_symbols()