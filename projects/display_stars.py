


def main():
    print()
    display_starts()
    print()

    display_starts(5)
    print()
    display_starts(7, 3)
    




def display_starts(cols=10, row=1):
    for row in range(row):
        for col in range(cols):
            print('*', end='')
        print()    


main()