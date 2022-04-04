import sys

def all_stocks():
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

    #preprocessing
    for i, param in enumerate(sys.argv):
        if (i != 0):
            split_params = param.split(',')
            for i, split_param in enumerate(split_params):
                split_params[i] = split_param.strip(' ')
                if (split_params[i] == ''):
                    exit(1)
        # case #1
            for split_param in split_params:            
                company = COMPANIES.get(split_param.capitalize())
                if (company != None):
                    print(split_param.capitalize(), "stock price is", STOCKS[company])
                    continue
        # case #2
                list = [x for x, y in COMPANIES.items() if y == split_param.upper()]
                if (len(list) != 0):
                    print(split_param.upper(), "is a ticker symbol for", list[0])
                    continue

                print(split_param, "is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()