import mysql.connector
from pessoa import Usuario


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

    def verifica_cadastro(self, user, email):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE user = %s OR email = %s', (user, email))
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            return True
        else:
            return False

    def cadastrar(self, p):
        if self.verifica_cadastro(p._user, p._email) == True:
            cursor.execute("INSERT INTO Usuarios (nome, email, endereco, user, senha) VALUES (%s, %s, %s, %s, %s)",
                           (p._nome, p._email, p._endereco, p._user, p._senha))
            conexao.commit()
            return True
        else:
            return False

    def logar(self, email, senha):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE email = %s AND senha = %s', (email, senha))
        resultado = cursor.fetchone()
        if resultado == None:
            return False
        else:
            return True
    def cad_jogo(self,nome,ano,descri,dica):
        cursor.execute('''INSERT INTO Jogos (nome,ano_lancamento,descri,dica) VALUES (%s, %s, %s, %s)''', (nome, ano, descri, dica))
        conexao.commit()


if __name__ == '__main__':
    import socket
    metodos = Metodos()
    ip = 'localhost'
    port = 8088
    addr = (ip, port)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    con, _ = serv_socket.accept()
    while True:
        try:
            msgLogin = con.recv(1024)
            mensagemStr = msgLogin.decode().split(',')
            enviar = ''
            if mensagemStr[0] == '1':
                email = mensagemStr[1]
                senha = mensagemStr[2]
                print('connectado1')
                if not metodos.logar(email, senha):
                    enviar = '1'
                else:
                    enviar = '0'
            elif mensagemStr[0] == '2':
                nome = mensagemStr[1]
                email = mensagemStr[2]
                endereco = mensagemStr[3]
                user = mensagemStr[4]
                senha = mensagemStr[5]
                print('connectado2')
                p = Usuario(nome, email, endereco, user, senha)
                if metodos.cadastrar(p):
                    enviar = '1'
                else:
                    enviar = '0'
            elif mensagemStr[0] == '3':
                nome = mensagemStr[1]
                ano_lancamento = mensagemStr[2]
                descri = mensagemStr[3]
                dica = mensagemStr[4]
                print('connectado3')
                metodos.cad_jogo(nome,ano_lancamento,descri,dica)
                enviar = '1'
        

            con.send(enviar.encode())

        except Exception as e:
            print('Email ou senha incorretos', str(e))
            con.close()
            break
        
