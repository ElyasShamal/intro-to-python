

import pickle
def main():
    end_of_file = False

    with open('info.data', 'rb') as data_file:
        while not end_of_file:
            try:
                person = pickle.load(data_file)
                display_data(person)
                
            except EOFError:    
                end_of_file = True


def display_data(person):
    print('Name:', person['name'])
    print('Street Number:', person['street number'])
    print('Street Name:', person['street name'])
    print('*' * 20)

if __name__ == '__main__':
    main()
