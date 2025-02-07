from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', titulo="Testando Vercel")

@app.route('/2')
def hello_world2():
    return render_template('Teste2.html')


if __name__ == '__main__':
    app.run()
