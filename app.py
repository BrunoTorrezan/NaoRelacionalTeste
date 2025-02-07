from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',titulo ="Escolha uma opção")

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', titulo ="Cadastro Não Relacional" )

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', titulo ="Exibir")


if __name__ == '__main__':
    app.run()
