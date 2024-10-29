

# order 1 - 12 1.50 each
# 12 or more  75 cent each



num_order = float(input("How many ice cream would you like to order: "))

PRICE_WITH_OUT_DISCOUNT = 1.50
PRICE_WITH_DISCOUNT = 0.75

if num_order <= 12:
    price = num_order * PRICE_WITH_OUT_DISCOUNT
else:
    price = (12 * PRICE_WITH_OUT_DISCOUNT) + ((num_order - 12 ) * PRICE_WITH_DISCOUNT)    

print(f'Your total is ${price:,.2f}.')    