from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Pessoa

app = Flask(__name__)
app.secret_key = 'chave_segura'

# Configuração do banco de dados SQLite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Cria o banco de dados e as tabelas

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    pessoas = Pessoa.query.all()
    return render_template('index.html', pessoas=pessoas)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        nova_pessoa = Pessoa(nome=nome, email=email)
        db.session.add(nova_pessoa)
        db.session.commit()
        flash(f'{nome} foi cadastrado(a) com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('cadastro.html')
if __name__ == '__main__':
    app.run(debug=True)
