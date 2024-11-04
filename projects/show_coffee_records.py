# This program show the coffee detail from coffe.txt


def main():
    with open('coffee.txt', 'r')as coffee_file:
        description = coffee_file.readline()

        while description != '':
            quantity = float(coffee_file.readline())
            description = description.rstrip('\n')

            print(f'Description: {description}')
            print(f'Quantity: {quantity}')

            description = coffee_file.readline()

if __name__ == '__main__':
    main()        