

# 1. Get desired future value from the user.
# 2. Get the anual interest rate.
# 3. Get the number of years that the money will appreciate.
# 4. Calculate the amount needed to deposit.
# 5. Display the amount needed to deposit


future_value = float(input('Enter the desired future value: '))
interest_rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the money will grow: '))
present_value = future_value / (1.0 + interest_rate)**years


print('You will need to deposit this amount:', round(present_value, 2))