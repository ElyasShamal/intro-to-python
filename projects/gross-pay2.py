

def main():
    try:
        hours = int(input('How mony hours did you work? '))
        paye_rate = float(input('Enter your hourly pay rate: '))

        gross_pay = hours * paye_rate

        print(f'Gross pay {gross_pay:,.2f}')
    except ValueError:
        print('Error: Hours worked and hourly pay rate must be valid numbers.')


if __name__ == "__main__":
    main()