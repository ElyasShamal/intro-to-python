

import pickle


phonebook = {'Elyas': '1222-444-55', 'jone': '222-222-222', 'danial':'444-222-344', 'Mohammad ELyas': '0000000000000000'}

with open('phonebook.dat', 'wb') as output_file:
    pickle.dump(phonebook, output_file)



with open('phonebook.dat', 'rb') as data_file:
    pb = pickle.load(data_file)


print(pb)



