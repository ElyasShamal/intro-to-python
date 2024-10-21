
# This program deminstrates how a floating point 
# number can be rounded.
# using round() method and f 

amount_due = 5000.0
monthly_payment = amount_due / 12.0

print(f'The montly payment is {monthly_payment:.2f}')
print('The montly payment is', round(monthly_payment, 2))