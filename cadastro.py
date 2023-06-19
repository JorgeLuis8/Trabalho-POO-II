import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cadastro"
)
cursor = conexao.cursor()


class Metodos:
    def __init__(self) -> None:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
        idUsuarios INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45) NOT NULL,
        email VARCHAR(45) NOT NULL,
        endereco VARCHAR(45) NOT NULL,
        user VARCHAR(45) NOT NULL,
        senha VARCHAR(45) NOT NULL
    )   ENGINE=InnoDB
        """)

        cursor.execute(""" CREATE TABLE IF NOT EXISTS Jogos (
        idJogos INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL,
        ano_lancamento DATE NOT NULL,
        descri VARCHAR(500) NOT NULL,
        dica LONGTEXT NOT NULL,
        PRIMARY KEY (idJogos))
        ENGINE = InnoDB;
        """)

    def cadastrar(self, p):
        cursor.execute("INSERT INTO Usuarios (nome, email, endereco, user, senha) VALUES (%s, %s, %s, %s, %s)",
                       (p._nome, p._email, p._endereco, p._user, p._senha))
        conexao.commit()
        return True

    def verifica_cadastro(self, user, email):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE user = %s OR email = %s', (user, email))
        resultado = cursor.fetchone()
        if resultado is not None:
            return True
        else:
            return False

    def login(self, email, senha):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE email = %s AND senha = %s ', (email, senha))
        resultado = cursor.fetchall()
        if len(resultado) == 0 :
            return False
        else:
            return True

    def verifica_tamsenha(self, senha):
        if len(senha) < 8:
            return True
        else:
            return False

    def verifica_tamuser(self, user):
        if len(user) < 6:
            return True
        else:
            return False 

    def exibir(self):
        cursor.execute('SELECT * FROM Usuarios')
        a = cursor.fetchall()
        for row in a:
            print(row)

    def exibirj(self):
        cursor.execute('SELECT * FROM Jogos')
        a = cursor.fetchall()
        for row in a:
            print(row)

    def cad_jogos(self, j):
        cursor.execute("""INSERT INTO Jogos (nome, ano_lancamento, descri, dica) VALUES (%s, %s, %s, %s)""",
                       (j._nome, j._ano_lancamento, j._desc, j.dica))
        conexao.commit()
        return True


a = Metodos()
a.exibir()
a.exibirj()
