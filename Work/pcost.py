# pcost.py
#
# Exercise 1.27

import csv
import sys
import stock

def portfolio_cost(filename):
    """
    Returns the total cost for all shares from 'filename'
    """
    total_cost = 0
    stocks = []
    with open(filename) as fp:
        rows = csv.reader(fp)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                stock_num = int(record['shares'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                stock_num = 0
            try:
                stock_price = float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                stock_price = 0.0
            
            stocks.append(stock.Stock(str(record['name']), stock_num, stock_price))

    total_cost = sum([holding.cost() for holding in stocks])
    return total_cost

if __name__ == '__main__':
    # accept input from command line
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print(f"The total cost for all the shares in {filename} is {cost:.2f}")
