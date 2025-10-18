from comunidadeimpressionadora import app,database
from comunidadeimpressionadora.models import Usuario
from flask import render_template, url_for, request, flash, redirect
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_criar_conta = FormCriarConta()
    form_login = FormLogin()

    if form_criar_conta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        user = Usuario(username=form_criar_conta.username.data, email=form_criar_conta.email.data, senha=form_criar_conta.senha.data)
        database.session.add(user)
        database.session.commit()
        flash(f'Conta criada com sucesso para o e-mail: {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_criar_conta=form_criar_conta, form_login=form_login)