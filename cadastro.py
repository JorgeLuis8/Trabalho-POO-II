import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
     database="mydb" )
cursor = conexao.cursor()

class metodos:
    def __init__(self) -> None:
        cursor.execute(
            "CREATE SCHEMA IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8")
        cursor.execute("USE mydb")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                idUsuarios INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(45) NOT NULL,
                email VARCHAR(45) NOT NULL,
                endereco VARCHAR(45) NOT NULL,
                cpf VARCHAR(45) NOT NULL,
                senha VARCHAR(45) NOT NULL,
                PRIMARY KEY (cpf)
            ) ENGINE = InnoDB;
        """)
        conexao.commit()

    def cadastrar(self,p):
        cursor.execute("INSERT INTO Usuarios (nome,email,endereco,cpf,senha) VALUES (%s,%s,%s,%s,%s)",(p._nome,p._email,p._endereco,p._cpf,p._senha))
        conexao.commit()
        return True
    def verifica_cadastro(self,cpf):
        cursor.execute('SELECT * FROM usuarios WHERE cpf = %s',(cpf,))
        resultado = cursor.fetchone()
        if resultado is not  None:
            return True
        else:
            return False
    def exibir(self):
        cursor.execute("SELECT * FROM Usuarios")
        resultado = cursor.fetchall()
        for i in resultado:
            print(i)
conexao.commit()
metodos.exibir(metodos)