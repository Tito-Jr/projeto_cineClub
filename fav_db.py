import sqlite3 as sql

con = sql.connect ('fav_db.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS fav')

sql = '''CREATE TABLE "fav" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOME" TEXT,
    "S" TEXT
    )'''

cur.execute(sql)
con.commit()

con.close()