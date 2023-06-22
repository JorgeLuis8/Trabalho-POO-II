import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cadastro"
)
cursor = conexao.cursor()

conexao.commit()

def cadastrarJogos(self,p):
    cursor.execute("INSERT INTO Jogos (nome, ano_lancamento) VALUES (%s, %s)",
                    (p._nome, p._ano_lancamento))
    conexao.commit()
    return True