from flask import Flask,render_template,request,redirect
import requests

def Estados():
    listadeestados=[]
    estados = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados").json()
    for estado in estados:
        listadeestados.append(estado['sigla'])
    listadeestados.sort()
    return listadeestados

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',titulo ="Escolha uma opção")

@app.route('/cadastro')
def cadastro():
    estados = Estados()
    return render_template('Cadastro.html', titulo ="Cadastro Não Relacional", estados=estados)

if __name__ == '__main__':
    app.run()
