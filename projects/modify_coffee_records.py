## open the otginal file for input and create a temporary file for output.
# Get the description of the records from user to be modified and the new value for the quantity.
# Read the first description field from orginal file .
# while description is not empty.
# read the quantity filed.
# if this desctiption field match with the descriprion entered:
# write the new data to emporary file .
# else : write the existing records to the temporary file.
# read the next description field.
# close the original file and the temporary file 
# delete the original file 
# rename the temporary file give it name of orginal file name.


# This is program allows the user to modify the quantity in a record in the coffee.txt


import os # need to remove and rename the files.

def main():


    found = False

    user_search = input('Enter a description to search for:  ')
    new_quantity = int(input('Enter the new quantity: '))

    with open('coffee.txt', 'r') as original_file , open('tem.txt', 'w') as tem_file:
        desc = original_file.readline()

        while desc != '':
            quantity = float(original_file.readline())
            desc = desc.rstrip('\n')
            if desc == user_search:
                tem_file.write(f'{desc}\n')
                tem_file.write(f'{new_quantity}\n')
                found = True
            else:
                tem_file.write(f'{desc}\n')
                tem_file.write(f'{quantity}\n')    
            desc = original_file.readline()    
    os.remove('coffee.txt')
    os.rename('tem_txt', 'coffee.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')    


if __name__ == '__main__':
    main()

