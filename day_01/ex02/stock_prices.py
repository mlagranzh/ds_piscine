import sys

def stock_prices():
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
            company = COMPANIES.get(param.capitalize())
            if (company == None):
                print("Unknown company")
            else:
                print(STOCKS[company])
            # print(type(string))


if __name__ == '__main__':
    stock_prices()