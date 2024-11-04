

# This program add coffee records to the coffee.txt file


def main():
    another = 'y'

    with open('coffee.txt', 'a') as coffee_file:
        while another == 'y' or another == "Y":
            print("Enter the following coffee data: ")
            description = input('Description: ')
            quantity = int(input('Quantity (in pounds): '))

            coffee_file.write(f'{description}\n')
            coffee_file.write(f'{quantity}\n')

            print('Do you want to add another coffee?')
            another = input('Y = Yes, N = No:  ')

    print('Data appended to coffee.txt.')


if __name__ == '__main__':
    main()