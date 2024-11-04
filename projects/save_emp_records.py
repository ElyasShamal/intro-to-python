
# This program gets employee data from user and saves it as a records in the employee.txt file 


def main():
    
    number_of_employees = int(input('How many employee records do you want to create ?  '))

    with open ('employee.txt', 'w') as employee_file:
        for count in range (1, number_of_employees + 1):
            print(f'Enter data for employee # {count}')
            name = input(f'Employee Name:  ')
            id_num = input(f'Id Number: ')
            dept = input('Department:  ')

            employee_file.write(f'Name: {name}\n')
            employee_file.write(f'Id Number: {id_num}\n')
            employee_file.write(f'Department: {dept}\n\n')

            print()

    print("Employee data submited!")        


if __name__ == '__main__':
    main()