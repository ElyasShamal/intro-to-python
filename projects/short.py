
# write a program that create my_file and add number from 1 to 100 using for loop



def main():
    my_file = open('my_file', 'w')
    for count in range(1, 101):
        my_file.write(f'{count}\n')
    my_file.close()
    print('Data submited!')

if __name__ == '__main__':
    main()



