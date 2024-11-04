


def main():
    number_of_days = int(input('For how many dayss do you have sales? '))
    sales_file = open('sales.text', 'w')

    for days_count in range(1, number_of_days + 1):
        sales = float(input(f'Enter the sales for the day #{days_count}: '))
        sales_file.write(f'{sales}\n')

    sales_file.close()
    print('Data written to sales.txt.')


if __name__ == '__main__':
    main()


