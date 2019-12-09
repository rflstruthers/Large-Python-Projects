##Python: 3.7.4
##Author: Reilly Struthers
##Purpose: Python course database drill.

import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def create_db(): # create db and table and column, call on get_txt()
    conn = sqlite3.connect('db_drill.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_text_files TEXT UNIQUE)')
        conn.commit()
    conn.close()
    get_txt()

def get_txt():
    # get .txt files from fileList and put them in a list, call on addToDb()
    txtFiles = []
    for names in fileList:
        if names.endswith('.txt'):
            txtFiles.append(names)
    addToDb(txtFiles)

def addToDb(txtFiles): # add list of .txt files to table in db, call on display_txt()
    conn = sqlite3.connect('db_drill.db')
    with conn:
        cur = conn.cursor()
        # add data to each column
        cur.execute('INSERT OR IGNORE INTO tbl_txtFiles(col_text_files) \
                    VALUES (?)',('{}'.format(txtFiles[0]),))
        cur.execute('INSERT OR IGNORE INTO tbl_txtFiles(col_text_files) \
                    VALUES (?)',('{}'.format(txtFiles[1]),))
        conn.commit()
    conn.close()
    display_txt()

def display_txt(): # select text files from table and print them
    conn = sqlite3.connect('db_drill.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT col_text_files FROM tbl_txtFiles')
        txt = cur.fetchall() # get everything from cur
        
        print('The Text files are: \n')
        
        for i in txt:
            print(*i, sep = "\n") 
    conn.close()

if __name__ == '__main__':    
    create_db()
