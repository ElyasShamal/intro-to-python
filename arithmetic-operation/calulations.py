

# Python performs arithmetic operations and Operators are used to perform various operations on variables and values like.
# addition, subtraction, multiplication, and division with +, -, *, and /.

# Addition, +, which returns the sum of two numbers.
# Subtraction, -, which returns the difference of two numbers.
# Multiplication, *, which returns the product of two numbers.
# Division, /, which returns the quotient of two numbers.
# Exponentiation, **, which returns the value of one number raised to the power of another.
# Modulus, %, which returns the remainder of one number divided by another.
# Floor division, //, which returns the integer quotient of two numbers.

print("_____________________________ First Part _____________________________")

# addition 
one = 10
two = 20 
print(one + two)  # = 30 


_salary = 2000
_bonus = 500
total_pay = _salary + _bonus

print(total_pay)  # 2500 


# subtraction 
total_pay = _salary - _bonus
print(total_pay)

# multiplication
total_pay = _salary * 12
print(total_pay)

quilt_width = 8
quilt_length = 12
print(quilt_width * quilt_length) # 96

quilt_length = 8 # reasign the quilt_length to 8 
print(quilt_width * quilt_length) # 64



#division
total_pay =  36000
montly_pay = total_pay / 12
print(montly_pay)


print("_______________________________ Sec Part _________________________________")

# Exponents

# Calculation of squares for:
# 6x6 quilt
print(6 * 6)

# 7x7 quilt

print(7 * 7)

# 8x8 quilt

print(8 * 8)

# How many squares for 6 people to have 6 quilts each that are 6x6?

print(6 ** 4)


print("_______________________________ Third Part _________________________________")

# Modulo 

# Python offers a companion to the division operator called the 
# A modulo calculation returns the remainder of the division between two numbers. 
# The modulo operator is indicated by % and gives the remainder of a division calculation. If the two numbers are divisible, then the result of the modulo operation will be 0.


# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)


print(3 % 3) # Prints 0
print(4 % 3) # Prints 1
print(5 % 3) # Prints 2
print(6 % 3) # Prints 0
print(7 % 3) # Prints 1


print("_______________________________ Challenge Part _________________________________")

#  You are starting a new campaign for your online shop where every 10th customer gets 10% off their next order.
#  To easily calculate this, you decide that order numbers divisible by 10 will receive the coupon

first_order_remainder = 269 % 10
print(first_order_remainder)
first_order_coupon = "No!"
print(first_order_coupon)

second_order_remainder = 270 % 10
print(second_order_remainder)
second_order_coupon = "Yes!"
print(second_order_coupon)