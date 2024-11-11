

def main():
    
    filename = input('Enter the file name: ')
    try:
        with open(filename, 'r') as check_data:
            content_of_file = check_data.read()
            print(content_of_file)
    except FileExistsError:
        print(f'The file {filename} does not exit.')

if __name__ == "__main__":
     main()                