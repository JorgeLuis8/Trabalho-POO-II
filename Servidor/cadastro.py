import mysql.connector
from pessoa import Usuario
from jogos import Jogos
from dica import Dica

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
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS `cadastro`.`dicas` (
    iddicas INT NOT NULL AUTO_INCREMENT,
    dica LONGTEXT NOT NULL,
    jogos_idJogos INT NOT NULL,
    usuarios_idUsuarios INT NOT NULL,
    PRIMARY KEY (iddicas),
    INDEX fk_dicas_jogos_idx (jogos_idJogos ASC) VISIBLE,
    INDEX fk_dicas_usuarios1_idx (usuarios_idUsuarios ASC) VISIBLE,
    CONSTRAINT fk_dicas_jogos
        FOREIGN KEY (jogos_idJogos)
        REFERENCES `cadastro`.`jogos` (idJogos)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT fk_dicas_usuarios1
        FOREIGN KEY (usuarios_idUsuarios)
        REFERENCES `cadastro`.`usuarios` (idUsuarios)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
    )
    ENGINE = InnoDB;
    """)

    def cadastrar(self, p):
        if self.verifica_cadastro(p._user, p._email):
            cursor.execute("INSERT INTO Usuarios (nome, email, endereco, user, senha) VALUES (%s, %s, %s, %s, %s)",(p._nome, p._email, p._endereco, p._user, p._senha))
            conexao.commit()
            return True

    def verifica_cadastro(self, user, email):
        cursor.execute(
        'SELECT * FROM Usuarios WHERE user = %s OR email = %s', (user, email))
        resultado = cursor.fetchone()
        if resultado == None:
            return True
        else:
            return False


    def login(self, email, senha):
        cursor.execute(
            'SELECT * FROM Usuarios WHERE email = %s AND senha = %s', (email, senha))
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
        cursor.execute("""INSERT INTO Jogos (nome, ano_lancamento, descri) VALUES (%s, %s, %s)""",
                       (j._nome, j._ano_lancamento, j._desc,))
        conexao.commit()
        return True
    def cadDica(self,d):
        cursor.execute(""" INSERT INTO dicas VALUES (%s)""",d.dicas)
        return True

if __name__ == '__main__':
    import socket
    metodos = Metodos()
    ip = 'localhost'
    port = 8089
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
                if metodos.login(email, senha):
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
                desc = mensagemStr[3]
                dica = mensagemStr[4]
                print('connectado3')
                j = Jogos(nome, ano_lancamento, desc, dica)
                if metodos.cad_jogos(j):
                    enviar = '1'
                else:
                    enviar = '0'
            elif mensagemStr[0] == '4':
                dica = mensagemStr[1]
                print('conectado4')
                d = Dica(dica)
                metodos.cadDica(d)
                
        
            con.send(enviar.encode())

        except Exception as e:
            print('Email ou senha incorretos', str(e))
            con.close()
            break
