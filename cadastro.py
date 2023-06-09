import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cadastro"
)
cursor = conexao.cursor()

conexao.commit()


class Metodos:
    def __init__(self) -> None:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
        idUsuarios INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45) NOT NULL,
        email VARCHAR(45) NOT NULL,
        endereco VARCHAR(45) NOT NULL,
        cpf VARCHAR(45) NOT NULL,
        senha VARCHAR(45) NOT NULL
    ) ENGINE=InnoDB
        """)

        conexao.commit()

    def cadastrar(self, p):
        cursor.execute("INSERT INTO Usuarios (nome, email, endereco, cpf, senha) VALUES (%s, %s, %s, %s, %s)",
                       (p._nome, p._email, p._endereco, p._cpf, p._senha))
        conexao.commit()
        return True

    def verifica_cadastro(self, cpf, email):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE cpf = %s OR email = %s', (cpf, email))
        resultado = cursor.fetchone()
        if resultado is not None:
            return True
        else:
            return False

    def login(self, email, senha):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE email = %s AND senha = %s', (email, senha))
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            return False
        else:
            return True

    def verifica_tamsenha(self, senha):
        if len(senha) < 8:
            return False
        else:
            return True

    def exibir(self):
        cursor.execute('SELECT * FROM Usuarios')
        a = cursor.fetchall()
        for row in a:
            print(row)


conexao.commit()

a = Metodos().exibir()
