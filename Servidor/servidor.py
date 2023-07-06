import mysql.connector
from pessoa import Usuario
import socket
import threading


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
        data_nas DATE NOT NULL NOT NULL,
        user VARCHAR(45) NOT NULL,
        senha VARCHAR(45) NOT NULL
    )   ENGINE=InnoDB
        """)

    cursor.execute(""" CREATE TABLE IF NOT EXISTS Jogos (
        idJogos INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL,
        ano_lancamento VARCHAR(100) NOT NULL,
        descri TEXT NOT NULL,
        dica TEXT NOT NULL,
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
            cursor.execute("INSERT INTO Usuarios (nome, email, data_nas, user, senha) VALUES (%s, %s, %s, %s, %s)",
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
            return True
        else:
            return False
    def cad_jogo(self,nome,ano,descri,dica):
        cursor.execute('''INSERT INTO Jogos (nome,ano_lancamento,descri,dica) VALUES (%s, %s, %s, %s)''', (nome, ano, descri, dica))
        conexao.commit()
        return True

    def listar_jogos(self,nome):
        cursor.execute('SELECT * FROM Jogos WHERE nome = %s', (nome,))
        resultado = cursor.fetchall()
        return resultado
    def listar_clientes(self,email):
        cursor.execute('SELECT * FROM Usuarios WHERE email = %s', (email,))
        resultado = cursor.fetchone()
        return resultado
class MyThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.name = ''
        self.client_socket = client_socket
        print('Nova conexão, endereço: ', client_address)
    
    def run(self):
        con = self.client_socket
        metodos = Metodos()
        while True:
            try:
                msgLogin = con.recv(1024)
                mensagemStr = msgLogin.decode().split(',')
                
                enviar = ''
                if mensagemStr[0] == '1':
                    email = mensagemStr[1]
                    senha = mensagemStr[2]
                    print('Conectado 1')
                    if not metodos.logar(email, senha):
                        enviar = '1'
                    else:
                        enviar = '0'
                elif mensagemStr[0] == '2':
                    nome = mensagemStr[1]
                    email = mensagemStr[2]
                    data_nas = mensagemStr[3]
                    user = mensagemStr[4]
                    senha = mensagemStr[5]
                    print('Conectado 2')
                    p = Usuario(nome, email, data_nas, user, senha)
                    if metodos.cadastrar(p):
                        enviar = '1'
                    else:
                        enviar = '0'
                elif mensagemStr[0] == '3':
                    nome = mensagemStr[1]
                    ano_lancamento = mensagemStr[2]
                    descri = mensagemStr[3]
                    dica = mensagemStr[4]
                    print('Conectado 3')
                    metodos.cad_jogo(nome, ano_lancamento, descri, dica)
                    enviar = '1' 
                elif mensagemStr[0] == '4':
                    nome = mensagemStr[1]
                    print('Conectado 4')
                    resultado = metodos.listar_jogos(nome)
                    if resultado:
                        resul = f'{resultado}'
                        print(resul)
                        con.send(resul.encode())
                    else:
                        enviar = '0'
                elif mensagemStr[0] == '5':
                    email = mensagemStr[1]
                    print('Conectado 5')
                    resultado = metodos.listar_clientes(email)
                    if resultado:
                        result = f'{resultado}'
                        con.send(result.encode())
                    else:
                        enviar = '0'
                con.send(enviar.encode())
            except ConnectionResetError:
                print('A conexão foi redefinida pelo cliente.')
                con.close()
                break
            except Exception as e:
                print('Erro ao processar a mensagem:', str(e))
                con.close()
                break

            
if __name__ == '__main__':
    metodos = Metodos()
    ip = '192.168.18.145'
    port = 8004
    addr = ((ip, port))
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    print('Aguardando conexão...')
    while True:
        print('teste')
        serv_socket.listen(10)
        client_socket, addr = serv_socket.accept()
        my_thread = MyThread(addr, client_socket)
        my_thread.start()
    
