import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = bd.cursor()
class cadastro:
    def __init__(self):
        cursor.execute("CREATE SCHEMA IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8")
        cursor.execute("USE mydb")

        # Criando a tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                idUsuarios INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(45) NOT NULL,
                email VARCHAR(45) NOT NULL,
                endereco VARCHAR(45) NOT NULL,
                cpf VARCHAR(45) NOT NULL,
                senha VARCHAR(45) NOT NULL,
                PRIMARY KEY (idUsuarios)
            ) ENGINE = InnoDB;
        """)
    def cadastro(self,parameters):
        cursor.execute

cursor.close()
bd.close()


cursor = bd.cursor()
