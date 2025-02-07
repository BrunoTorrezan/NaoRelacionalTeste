from flask import Flask,render_template,request,redirect
from tinydb import TinyDB
import requests

def Estados():
    listadeestados=[]
    estados = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados").json()
    for estado in estados:
        listadeestados.append(estado['sigla'])
    listadeestados.sort()
    return listadeestados

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

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    datanas = request.form['datanas']
    genero = request.form.get('gender')
    endereco = request.form['endereco']
    estado = request.form['estado']
    cidade = request.form['cidade']
    Dado = {'nome':nome,'telefone':telefone,
            'DataNascimento':datanas,'Genero':genero,
            'Endereco':endereco,'Estado':estado,'Cidade':cidade}
    db.insert(Dado)
    return redirect('/exibir')

@app.route('/excluir/<id>')
def excluir(id):
    db.remove(doc_ids=[int(id)])
    return redirect('/exibir')

@app.route('/editar/<id>')
def editar(id):
    estados = Estados()
    dado = db.get(doc_ids=[int(id)])
    return render_template('Editar.html',id=id, dado = dado[0], titulo='Editar Item',estados=estados)

@app.route('/alterar/<id>', methods=['POST'])
def alterar(id):
    nome = request.form['nome']
    telefone = request.form['telefone']
    datanas = request.form['datanas']
    genero = request.form.get('gender')
    endereco = request.form['endereco']
    estado = request.form['estado']
    cidade = request.form['cidade']
    db.update({'nome':nome,'telefone':telefone,
            'DataNascimento':datanas,'Genero':genero,
            'Endereco':endereco,'Estado':estado,'Cidade':cidade},doc_ids=[int(id)])
    return redirect('/exibir')

if __name__ == '__main__':
    app.run()
