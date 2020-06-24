# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Reads the given portfolio file into a list of tuples.'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                holding = { 'name': record['name'], 
                            'shares': int(record['shares']), 
                            'price': float(record['price']) }

                portfolio.append(holding)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return portfolio


def read_prices(filename):
    '''Reads the given portfolio file and store the shares' price into a dict.'''
    prices = {}

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])

    return prices


def make_report(portfolio, prices):
    """Reads portfolio and price data from 'portfolio' and 'prices'
       respectively to compute gain/loss in the share's price.
    """
    
    gain_list = []

    for record in portfolio:
        share_name = record['name']
        if share_name in prices:
            gain = prices[share_name] - record['price']
            gain_list.append((share_name, record['shares'], prices[share_name], gain))
    
    return gain_list

def printer(gain_list, delimiter_symbol='-'):
    """Formats and prints data from gain_list"""
    delimiter_base = delimiter_symbol * 10 + ' '
    delimiter = delimiter_base * 4
 
    headers = ('Name', 'Shares', 'Price', 'Change')   
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{delimiter}')
    
    for name, shares, price, change in gain_list:
        print(f'{name:>10s} {shares:>10d}', end=' ')

        int_price = int(price)
        if int_price < 10:
            price_formatter = f'{"$":>6}{price:<4.2f}'
        elif int_price >= 10 and int_price < 100:
            price_formatter = f'{"$":>5}{price:<5.2f}'
        else:
            price_formatter = f'{"$":>4}{price:<6.2f}'

        print(price_formatter, end=' ')
        
        print(f'{change:>10.2f}')

def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    '''Generates report from portfolio and price files.'''
    portfolio = read_portfolio(portfolio_filename)
    
    prices = read_prices(prices_filename)
    
    report = make_report(portfolio, prices)
    
    printer(report)

def main(args: list) -> None:
    '''Main function driver'''
    print(f'Running {args[0][:-2]}main...', end='\n\n')

    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
    else:
        main(sys.argv[:3])
