

## get the number of cups
# convert the number of cups to fluif ounce and display the result 



def main():
    intro()
    print()
    cups_needed = int(input('Enter the number of cups: '))
    cups_to_ounces(cups_needed)


def intro():
    print()
    print('This program converts measurements\n'
          'in cups to fluid ounce, For your \n'
          'reference the formula is \n'
          '1 cup = 8 fluid ounces')
    



def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That convert to {ounces} ounces.')


main()