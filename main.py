from flask import Flask, render_template, request

app = Flask('app')
import sqlite3

banco = "database.db"

conexao = sqlite3.connect(banco, check_same_thread=False)
cursor = conexao.cursor()




def inserir(t1, t2, t3, t4):
    cursor = conexao.cursor()
    cpf = t1
    placa = t2
    cel = t3
    vagas_n_vagas = t4
    cursor.execute("INSERT INTO carro (cpf, placa, cel, vagas_n_vagas) VALUES (?,?,?,?)",
                   (cpf, placa, cel, vagas_n_vagas))
    conexao.commit()


def pesquisar(v1):
    cursor = conexao.cursor()
    placa1 = v1
    cursor.execute("SELECT * FROM carro WHERE placa = ?", (placa1,))
    result = cursor.fetchall()
    print(result)
    return '''
    for i in result:
    print(i)
  '''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['POST'])
def cadastro():
    cpf = request.form['cpf']
    placa = request.form['placa']
    cel = request.form['cel']
    vagas_n_vagas = request.form['vagas_n_vagas']

    inserir(cpf, placa, cel, vagas_n_vagas)
    return 'Cadastro de %s %s realizado com sucesso! <br/> <a href="/">Voltar</a>' % (cpf, placa, cel, vagas_n_vagas)


@app.route('/consulta', methods=['POST'])
def consulta():
    placa = request.form['placa']
    pesquisar(placa)
    #  resultado()
    return '<a href="/">Voltar</a>'


app.run(host='localhost', port=8080)
conexao.close()
