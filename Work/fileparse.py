# fileparse.py

# Exercise 3.3
import csv

def parse_csv(filename: str, select=None, types=None, has_headers: bool=False, delimiter: str=' ') -> list:
    '''Parse a CSV file into a list of records'''

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if select and has_headers == False:
            raise RuntimeError("select argument requires column headers")

        # Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers userd for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:   # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # type conversion if types
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary
            record = dict(zip(headers, row)) if has_headers else tuple(row)
            records.append(record)
 
    return records
