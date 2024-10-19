
# what is string ?

# A string is a sequence of characters contained within a pair of single quotes (') or double quotes(").
# Strings can store words, sentences, or whole paragraphs. They can be any length and can contain letters, numbers, symbols, and spaces.

# Other data types such as integers, doubles, and booleans can also be strings if they are wrapped in quotes.

print('--------------------------------------------------------------------------------------------------------------')

# string with single quotes ' ' 

message_one = 'I am a String with single Quotes'
print(message_one)

# String with double quotes " "

message_two = "I am a string with double Quotes"
print(message_two)


# wrapped number in quotes 

number = '3'
print(number)
print(type(number)) # class str



# Accessing the Characters of a String
# strings in Python are technically a type of list — one in which each character is a separate element.
# This means each character in a string can be individually accessed by index, like with the elements in a list:

my_message = "Hi, welcome to python"

var_1 = my_message[0]
print(var_1) # H
var_2 = my_message[1]

var_3 = var_1 + var_2 + "!"
print(var_3)


# If an attempt is made to access an index out of bounds, it will return an IndexError.

name = "Elyas"  # index #
#name[7]
#print(name) # Throws an IndexError


# Multi-line Strings
# Strings can be long or short. For longer text, a multi-line string can be used. 
# Multi-line strings begin and end with three single or double quotes:

print('--------------------------------------------------------------------------------------------------------------')

my_message = """ If it
were done when 'tis done, then 'twere well It were done quickly: if the assassination
Could trammel up the consequence, and catch
With his surcease success; that but this blow
Might be the be-all and the end-all here,
But here, upon this bank and shoal of time,
We'ld jump the life to come.   """

print(my_message)

print('--------------------------------------------------------------------------------------------------------------')

# Escape Characters
# Sometimes a string may have a character that Python tries to interpret, such as '.

my_string = 'It\'s a lovely day!'

print(my_string)

note = "I am on top!\nI am on bottom. \n\tI am indented!"

print(note)


print('--------------------------------------------------------------------------------------------------------------')

my_message = """ If it
were done when 'tis done, then 'twere well It were done quickly: if the assassination
Could trammel up the consequence, and catch
With his surcease success; that but this blow
Might be the be-all and the end-all here,
But here, upon this bank and shoal of time,
We'ld jump the life to come.   """

if "come" in my_message:
    print("it's in there")


print('--------------------------------------------------------------------------------------------------------------')


# Comparing Strings
# Python can use comparison operators to compare the contents of two strings. The operators behave as they do with numeric arguments:

# ==	Equal	Returns True if two strings are equal.
# !=	Not equal	Returns True if two strings are not equal.
# <	Less than	Returns True if the left string is lexically prior the right string.
# >	Greater than	Returns True is the left string comes lexically after the right string.
# <=	Less than or equal to	Returns True if the left string is equal to or lexically prior to the right string.
# >=	Greater than or equal to  Returns True if the left string is equal to or comes lexically after the right string.

string_one = "Hello"
string_two = "World"

print(string_one > string_two)
print(string_one < string_two)


print('--------------------------------------------------------------------------------------------------------------')

# Built-in String Methods

# Python has a number of built-in string methods that manipulate strings.
# However, when these methods are called, the original string will not be changed, 
# so any modifications will need to be saved to a new variable. A few useful built-in string methods are listed below.


# .capitalize() Takes in a string, and returns a copy of the string in capital case.

my_name = 'elyas '
print(my_name.capitalize()) # convert my_name to capitalize


# .casefold() Returns a copy of the string with all characters in lowercase.

my_lastName = "SHAMAL"
print(my_lastName.casefold())


# .center() Returns a new string with the specified padding.

programming = "learning Python is fun!"
print(programming.center(160))


# .count() Finds the number of times the specified substring occurs within a given string.

say_hey = "heyyyyyyyyyyyyyyyyyy"
print(say_hey.count("y"))

# .endswith() Checks whether or not a string ends with a given value.

print(say_hey.endswith('y')) # True 


# .find() Takes in a substring (and optionally start/end index), return the index number of the first occurrence of the substring inside a string.
# string.find(substring, start, end)

new_string = "I like to eat potato"

print(new_string.find("like"))

# .format() Returns a string with values inserted via placeholders.

phrase = "I like to eat {}s and {}s."

formatted_phrase = phrase.format("apple", "orange")

print(formatted_phrase)



phrase_1 = "I like to eat {food1}s and {food2}s."
new_phrase_1 = phrase_1.format(food1="apple", food2="orange")

phrase_2 = "I like to eat {food2}s and {food1}s."
new_phrase_2 = phrase_2.format(food1="apple", food2="orange")

print(new_phrase_1)
print(new_phrase_2)