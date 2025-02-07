from flask import Flask,render_template,request,redirect
from tinydb import TinyDB


db = TinyDB('banco.json')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',titulo ="Escolha uma opção")

@app.route('/cadastro')
def cadastro():
    estados = Estados()
    return render_template('Cadastro.html', titulo ="Cadastro Não Relacional", estados=estados)

@app.route('/exibir')
def exibir():
    valores = [dict(record, doc_id=record.doc_id) for record in db]
    return render_template('Exibir.html', titulo ="Exibir", dados=valores)


if __name__ == '__main__':
    app.run()
