# pcost.py
#
# Exercise 1.27

# open portfolio file for reading
f = open('Data/portfolio.csv', 'rt')
# skip the header line
headers = next(f)

# hold the total cost
total_cost = 0

# iterate over the file to compute the total cost for the shares purchases
for line in f:
    stock_name, stock_num, stock_price = line.strip().split(',')
    try:
        stock_num = int(stock_num)
    except Exception:
        stock_num = 0
    try:
        stock_price = float(stock_price)
    except:
        stock_price = 0
    total_cost += stock_num * stock_price

# close the file
f.close()

print(f"The total cost for all the shares is {total_cost:.2f}")
