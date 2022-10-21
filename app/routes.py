from app import app
from flask import render_template
from flask import request
import sqlite3 as sql

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/registro.html')
def registro():
    return render_template('registro.html')

@app.route('/registrar', methods=["POST"])
def registrar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")

    con = sql.connect("usuarios_db.db")
    cur = con.cursor()
    cur.execute("insert into users(NOME, EMAIL, SENHA) values (?,?,?)", (nome, email, senha))
    con.commit()

    print('Dados recebidos (cadastro): ', nome, email, senha)

    return render_template('index.html')

@app.route('/favoritos', methods=["POST"])
def favoritos():
    titulo = request.data
    print('Dados recebidos (favorito)', titulo.decode())    
    con = sql.connect("fav_db.db")
    cur = con.cursor()
    cur.execute("insert into fav(NOME, S) values (?, ?)", (titulo, '1'))
    con.commit()
    return 'OK'

@app.route('/favoritos', methods=['GET'])
def listaFav():
    con = sql.connect("fav_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from fav")
    data = cur.fetchall()
    r = ''
    for i in data:
        print(i['NOME'])
        s = str(i['NOME']).replace('b\'', '').replace('\'', '')
        r += '-' + s
        print(s)


    return r
@app.route('/logar', methods=['POST'])
def logar():
    return render_template('index.html')

@app.route('/salvar_resenha', methods=["POST"])
def salvar_resenha():
    titulo = request.form.get("tituloFilme")
    nome = request.form.get("nome")
    email = request.form.get("email")
    resenha = request.form.get("resenha")
    con = sql.connect("resenhas_db.db")
    cur = con.cursor()
    cur.execute("insert into resenhas(FILME, NOME, EMAIL, RESENHA) values (?,?,?,?)", (titulo, nome, email, resenha))
    con.commit()
    print('Dados recebidos (resenha): ', titulo, nome, email, resenha)
    return render_template('index.html')

@app.route('/bdAllResenhas')
def bdAllResenhas():
    con = sql.connect("resenhas_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from resenhas")
    data = cur.fetchall()
    for i in data:
        print(i['FILME'], i['NOME'], i['EMAIL'], i['RESENHA'])
    return 'OK'

@app.route('/bdAllFav')
def bdAllFav():
    con = sql.connect("fav_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from fav")
    data = cur.fetchall()
    for i in data:
        print(i['NOME'])
    return 'OK'

@app.route('/bdAllUsuarios')
def bdAllUsuarios():
    con = sql.connect("usuarios_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    for i in data:
        print(i['NOME'], i['EMAIL'])
    return 'OK'

