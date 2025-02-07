from flask import Flask,render_template,request,redirect
from tinydb import TinyDB

db = TinyDB('banco.json')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',titulo ="Escolha uma opção")

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', titulo ="Cadastro Não Relacional")

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', titulo ="Exibir")

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



if __name__ == '__main__':
    app.run()
