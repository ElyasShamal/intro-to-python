
# This program allow user to search the coffee.txt 
# file for records matching a description

def main():


    found = False

    user_search = input('Enter a description to search for...:  ')

    with open('coffee.txt', 'r') as coffee_file:
        description = coffee_file.readline()

        while description != '':
            quantity = float(coffee_file.readline())
            description = description.rstrip('\n')

            
            if description == user_search:
                print(f'Description: {description}')
                print(f'Quantity: {quantity}')
                print()
                found = True

            description = coffee_file.readline()
    if not found:
        print('That item was not found in the file')   

if __name__ == '__main__':
    main()                   