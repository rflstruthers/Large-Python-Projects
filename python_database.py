

import sqlite3

conn = sqlite3.connect('python_test.db') # create and connect to db

with conn:
    cur = conn.cursor()
    # create table and add columns
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )')
    conn.commit()
conn.close()


conn = sqlite3.connect('python_test.db')

with conn:
    cur = conn.cursor()
    # add data to each column
    cur.execute('INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)', \
                ('Bob','Smith','bsmith@gmail.com'))
    cur.execute('INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)', \
                ('Sally','May','smay@gmail.com'))
    cur.execute('INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)', \
                ('Kevin','Bacon','kbacon@gmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('python_test.db')

with conn:
    cur = conn.cursor()
    # select statement
    cur.execute('SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE \
        col_fname = "Sally"')
    varPerson = cur.fetchall() # get everything from cur
    for item in varPerson:
        msg = 'First Name: {}\nLast Name: {}\nEmail: {}'.format(item[0],item[1],item[2])
    print(msg)
        



