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
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)

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

def printer(gain_list):
    """Formats and prints data from gain_list"""
    delimiter_base = '-' * 10 + ' '
    delimiter = delimiter_base * 4
    
    print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
    print(f'{delimiter}')
    
    for name, shares, price, change in gain_list:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)
    printer(report)
