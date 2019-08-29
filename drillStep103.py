import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
    for i in fileList:
        if i.endswith('.txt'):
            txtList = [(i)]
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)", txtList)
            print(txtList)
            conn.commit()
conn.close()
