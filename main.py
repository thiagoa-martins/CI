import os

from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave-padrao')

lista_de_usuarios = ['Thiago', 'Pedro', 'Munir', 'Vinicius', 'Ryan']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_de_usuarios=lista_de_usuarios)

@app.route('/login')
def login():
    form_criar_conta = FormCriarConta()
    form_login = FormLogin()
    return render_template('login.html', form_criar_conta=form_criar_conta, form_login=form_login)

if __name__ == '__main__':
    app.run(debug=True)

