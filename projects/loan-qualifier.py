
# This program determine whether abank customer 
# qualifies for a loan or not 


MIN_SALARY = 30000.0
MIN_YEARS = 2 

cutomer_salary = float(input('Enter your annual salary: '))
years_on_job = int(input('Enter number of years employed: '))

if cutomer_salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('Congratulation! you qualify for the loan')
    else:
        print(f'You must have been employed '
              f'for at least {MIN_YEARS} '
              f'years to qualify fo the loan.') 
else:
    print('You must earn at least $'
          f'{MIN_SALARY:,.2f} '
          f'per year to qualify for loan.')       



# if cutomer_salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
#     print('Congratulation! you qualify for the loan')
# else:
#     print('You must earn at least $'
#           f'{MIN_SALARY:,.2f} '
#           f'per year to qualify for loan.')  