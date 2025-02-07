from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', titulo="Testando Vercel")

@app.route('/cadastro')
def cadastro():
    estados = Estados()
    return render_template('Cadastro.html', titulo ="Cadastro Não Relacional", estados=estados)

if __name__ == '__main__':
    app.run()
