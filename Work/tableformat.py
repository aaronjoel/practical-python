# tableformat.py

class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print(f'<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print(f'</tr>')

    def row(self, rowdata):
        print(f'<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print(f'</tr>')

def create_formatter(name: str) -> TableFormatter:
    '''
    Create a TableFormatter object given the output extension.
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(list_of_portfolio: list, list_of_attrs: list, formatter) -> None:
    '''
    Print a nicely formatted table from a list of attributes
    '''
    formatter.headings(list_of_attrs)
    for portfolio in list_of_portfolio:
        row_data = [str(getattr(portfolio, attr_name)) for attr_name in list_of_attrs]
        formatter.row(row_data)
