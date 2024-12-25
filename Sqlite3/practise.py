



import sqlite3
# conn = sqlite3.connect('test.db')
# cur = conn.cursor()
# conn.commit()
# conn.clone()

def main():
    conn = sqlite3.connect('contact.db')
    cur = conn.cursor()

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()    