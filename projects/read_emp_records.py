

# This program display the record that are in the employee.txt file.



def main():
    
    with open('employee.txt', 'r') as employee_file:
        name = employee_file.readline()

        while name != '':
            id_num = employee_file.readline()
            dept = employee_file.readline()

            name = name.rstrip('\n')
            id_num = id_num.rstrip('\n')
            dept = dept.rstrip('\n')
         
            print(f'{name}')
            print(f'{id_num}')
            print(f'{dept}')
            name = employee_file.readline()

if __name__ == '__main__':
    main()