from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)

