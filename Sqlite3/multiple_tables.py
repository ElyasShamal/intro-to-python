

import sqlite3

def main():
    conn = sqlite3.connect('company.db')
    cur = conn.cursor()
    cur.execute('''  CREATE TABLE Customers (CustomerID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Email TEXT) ''')

    cur.execute(''' CREATE TABLE Employess (EmployeeID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Email, TEXT) ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()    

