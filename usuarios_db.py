import sqlite3 as sql

con = sql.connect ('usuarios_db.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOME" TEXT,
    "EMAIL" TEXT,
    "SENHA" TEXT
    )'''

cur.execute(sql)
con.commit()