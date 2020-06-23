# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str, select=None) -> list:
    '''Parse a CSV file into a list of records'''

    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers userd for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname if select]
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

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
 
    return records
