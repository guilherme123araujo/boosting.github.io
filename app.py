from flask import Flask, render_template, request
import mysql.connector
import smtplib

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='boosting',
)

cursor = conexao.cursor()

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_send.php', methods=['POST'])
def processar_formulario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    message = request.form.get('message')

    # Faça o processamento dos dados, se necessário
    # print(nome, email, message)
    # Exemplo: exibir os dados recebidos
    

    #Envio de dados para dbc (emails registrados - Tabela dos nomes e dos emails que já enviaram mensagens)
    comando = f'INSERT INTO registros (nome, email) VALUES ("{nome}", "{email}")'
    cursor.execute(comando) #Executa o comando determinado na variável "comando"
    # conexao.commit() 


    #Envio de email

    return render_template('index.html')



if __name__ == '__main__':
    app.run()
