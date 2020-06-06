# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
num_months = 0

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    num_months += 1
    if num_months <= 12:
        principal -= extra_payment
        total_paid += extra_payment
    

print(f'Total paid {total_paid:.1f} in {num_months} months')
