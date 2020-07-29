# ticker.py

from follow import follow
import csv
import report
import tableformat

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfolio_file: str, stock_file: str, format_ext: str) -> None:
    portfolio = report.read_portfolio(portfolio_file)
    stock_rows = parse_stock_data(follow(stock_file))
    rows = filter_symbols(stock_rows, portfolio)

    formatter = tableformat.create_formatter(format_ext)

    
    formatter.headings(['Name', 'Price', 'Change'])

    for row in rows:
        rowdata = [f'{data:0.2f}' if isinstance(data, float) else data for data in row.values()]
        formatter.row(rowdata)


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
