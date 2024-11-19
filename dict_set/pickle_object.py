

import pickle

def main():
    again = 'y'

    with open('info.data', 'wb') as info_data:
        while again.lower() == 'y':
            save_data(info_data)
            again = input('Enter more data? (y/n): ')


def save_data(file):
    person = {}

    person['name'] = input('Name: ')
    person['street number'] = int(input('Street Number: '))
    person['street name'] = input('Street Name: ')


    pickle.dump(person, file)


if __name__ == '__main__':
    main()    


