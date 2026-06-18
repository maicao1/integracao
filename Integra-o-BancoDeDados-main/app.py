# Import do framework flask
# Import do render_template para ler o HTML e busca ou o endereço do arquivo ou a URL
# request para capturar os dados
from flask import Flask, render_template, request

import mysql.connector 

# Para vincular as páginas e saberem ond estão:

app = Flask(__name__)

# Cria conexão com o mySQL
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}

# Criação de rota para o arquivo HTML principal

@app.route('/cadastrar', methods=['POST'])




def indexRota():
    return render_template('index.html')
# Biblioteca mysql.connector conecta o Python com o MySQL



@app.route('/cadastrar', methods=['POST'])
def criar_cadastro():

 try:



    cpf = request.form['cpf']
    primeiro_nome = request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    idade = request.form['idade']


    conexao = mysql.connector.connect(**bd_config)

    curso = conexao.cursor()

    query = "INSERT INTO cliente1(CPF,PRIMEIRO_NOME,SOBRENOME,IDADE)VALUES(%s,%s,%s,%s)"
    curso.execute(query(cpf,primeiro_nome,sobrenome,idade))
        
    curso.commit()
    curso.close()
    curso.close()


 except mysql.connector.error as err:
   return f"erro de conexao com o banco de dados"


