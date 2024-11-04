

def main():
    sales_file = open('sales.text', 'r')
    line = sales_file.readline()

    while line != '':
        amount = float(line)
        print(f'{amount:.2f}')

        line = sales_file.readline()
    sales_file.close()
    print('All data readed')


if __name__ == '__main__':
    main()        