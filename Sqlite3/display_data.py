


import sqlite3

def main():
    conn = sqlite3.connect('Contacts.db')  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    try:
        cur.execute(''' SELECT * FROM Contacts ''')  # Corrected SQL statement
        result = cur.fetchall()  # Fetch all rows from the result
        print(result)  # Print the result
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()  # Close the connection

if __name__ == "__main__":
    main()