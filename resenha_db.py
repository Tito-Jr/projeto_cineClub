import sqlite3 as sql

con = sql.connect ('resenhas_db.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS resenhas')

sql = '''CREATE TABLE "resenhas" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "FILME" TEXT,
    "NOME" TEXT,
    "EMAIL" TEXT,
    "RESENHA" TEXT
    )'''

cur.execute(sql)
con.commit()

con.close()

