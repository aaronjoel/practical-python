# report.py
#
# Exercise 2.4

import fileparse
import csv
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file, 
                                        select=['name', 'shares', 'price'],
                                        types=[str, int, float],
                                        **opts)

    #port = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    port = [stock.Stock(**d) for d in portdicts]
    return Portfolio(port)

def read_portfolio_(filename):
    '''Reads the given portfolio file into a list of tuples.'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                holding = stock.Stock(record['name'], 
                                      int(record['shares']), 
                                      float(record['price'])) 

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
        share_name = record.name
        if share_name in prices:
            gain = prices[share_name] - record.price
            gain_list.append((share_name, record.shares, prices[share_name], gain))
    
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

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename: str, prices_filename: str, fmt: str='txt') -> None:
    '''Generates report from portfolio and price files.'''
    
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    
    # Create the report data
    report = make_report(portfolio, prices)
    
    # commented out to make use of our new formatter class
    formatter = tableformat.create_formatter(fmt)

    # Print it out
    print_report(report, formatter)
  
def main(args: list) -> None:
    '''Main function driver'''
    print(f'Running {args[0][:-2]}main...', end='\n\n')

    portfolio_report(args[1], args[2], args[3])
    print()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
    else:
        main(sys.argv[:4])
