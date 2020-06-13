# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    """
    Returns the total cost for all shares from 'filename'
    """
    total_cost = 0
    with open(filename) as fp:
        rows = csv.reader(fp)
        headers = next(rows)
        for row in rows:
            stock_name, stock_num, stock_price = row
            try:
                stock_num = int(stock_num)
            except ValueError:
                stock_num = 0
            try:
                stock_price = float(stock_price)
            except ValueError:
                stock_price = 0.0
            total_cost += stock_num * stock_price
        return total_cost

if __name__ == '__main__':
    cost = portfolio_cost('Data/portfolio.csv')
    print(f"The total cost for all the shares is {cost:.2f}")
