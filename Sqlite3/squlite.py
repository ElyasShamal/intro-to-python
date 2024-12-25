

import sqlite3


def main():
    conn = sqlite3.connect('Contacts.db')
    cur = conn.cursor()
    cur.execute('''CREATE  TABLE  Contacts (ContactID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Email TEXT)''')
    cur.execute(''' INSERT INTO Contacts (ContactID, Name, Email) 
                VALUES (1, 'Elyas shamal', '123@gmail.com')''') 
    cur.execute(''' INSERT INTO Contacts (ContactID, Name, Email) 
                VALUES (2, 'shamal', 'sho@gmail.com')''') 
    cur.execute(''' INSERT INTO Contacts (ContactID, Name, Email) 
                VALUES (3, 'moshamal', 'Mo@gmail.com')''') 
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()



