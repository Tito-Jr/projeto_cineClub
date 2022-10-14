import pymysql.cursors

def initConn():
    conn = pymysql.connect(
        host='127.0.0.1', 
        user='root', 
        password='', 
        db='cineclube',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn

def select():
    conn = initConn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM favoritos')
    result = cursor.fetchall()

    r = ''
    for line in result:
        r += '-' + line['nomeDoFilme']
        print(r)
    
    cursor.close()

    return r

def insertFav(nome):
    conn = initConn()
    sql = 'INSERT INTO favoritos (nomeDoFilme) VALUES (%s)'
    cursor = conn.cursor()
    cursor.execute(sql, (nome))
    cursor.close()
    conn.commit()
    conn.close()
    print('Favorito adicionado com sucesso!')

def insert(nomeDoFilme, nome, email, resenha):
    conn = initConn()
    sql = 'INSERT INTO resenhas (nomeDoFilme, nome, email, resenha) VALUES (%s, %s, %s, %s)'
    cursor = conn.cursor()
    cursor.execute(sql, (nomeDoFilme, nome, email, resenha))
    cursor.close()
    conn.commit()
    conn.close()
    print('Dados Inseridos com sucesso!')