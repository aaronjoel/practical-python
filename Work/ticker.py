# ticker.py

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
