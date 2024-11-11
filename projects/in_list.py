
# this program demonstrates the in operator
# used with a list


def check_search():
    product_numbers = ['V475', 'F987', 'Q143', 'R688']
    
    user_search = input("Enter the product name: ")

    if user_search in product_numbers:
        print(f'{user_search} was found in the list.')
    else:
        print(f'{user_search} was not found in the list.')


if __name__ == 'check_search':
    check_search()
