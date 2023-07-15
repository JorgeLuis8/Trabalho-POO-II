import mysql.connector
from pessoa import Usuario
import socket
import threading
import json
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cadastro"
)
cursor = conexao.cursor()

class Metodos:
    """ 
    Classe usada para criar o banco de dados e realizar as operações de cadastro, login e listagem de clientes

    Attributes
    ----------
    conexao : mysql.connector.connect
        Conexão com o banco de dados
    cursor : mysql.connector.cursor
        Cursor para executar as operações no banco de dados
    

    
    Methods
    -------
    verifica_cadastro(user, email)
        Verifica se o usuário já está cadastrado no banco de dados
    cadastrar(p)
        Cadastra um novo usuário no banco de dados
    logar(email, senha)
        Verifica se o usuário está cadastrado no banco de dados
    listar_clientes(email)
        Lista os dados de um cliente específico
    listar_jogos(nome)
        Lista os dados de um jogo específico
    especifico(fase, nome)
        Lista os dados de um jogo específico

    """
    def __init__(self):
        """ 
        Parameters
        ----------
        conexao : mysql.connector.connect
            Conexão com o banco de dados
        cursor : mysql.connector.cursor
            Cursor para executar as operações no banco de dados

    Returns
    -------
    None

        """
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            idUsuarios INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(45) NOT NULL,
            email VARCHAR(45) NOT NULL,
            data_nas DATE NOT NULL,
            user VARCHAR(45) NOT NULL,
            senha VARCHAR(45) NOT NULL
        ) ENGINE=InnoDB
        """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS jogos (
        idJogos INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL,
        fase TEXT NOT NULL,
        descri TEXT NOT NULL,
        dica TEXT NOT NULL,
        PRIMARY KEY (idJogos))
        ENGINE = InnoDB
        AUTO_INCREMENT = 24
        DEFAULT CHARACTER SET = utf8mb4
        COLLATE = utf8mb4_0900_ai_ci;""")
        conexao.commit()

  
    def verifica_cadastro(self, user, email):
        """ 
        Verifica se o usuário já está cadastrado no banco de dados

        Parameters
        ----------
        user : str
            Nome de usuário
        email : str
            Endereço de e-mail
        
        Returns
        -------
        bool
            True se o usuário não está cadastrado, False caso contrário

        Returns
        -------
        bool
            True se o usuário não está cadastrado, False caso contrário
        
        
        """
        cursor.execute(
            'SELECT * FROM Usuarios WHERE user = %s OR email = %s', (user, email))
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            return True
        else:
            return False

    def cadastrar(self, p):
        """
        Cadastra um novo usuário no banco de dados
        
        Parameters
        ----------
        p : Pessoa
            Objeto da classe Pessoa

        Returns
        -------
        bool
            True se o usuário foi cadastrado com sucesso, False caso contrário
        
        

        """
        if self.verifica_cadastro(p._user, p._email) == True:
            cursor.execute("INSERT INTO Usuarios (nome, email, data_nas, user, senha) VALUES (%s, %s, %s, %s, %s)",
                           (p._nome, p._email, p._endereco, p._user, p._senha))
            conexao.commit()
            return True
        else:
            return False

    def logar(self, email, senha):
        """ 
        Verifica se o usuário está cadastrado no banco de dados e se a senha está correta 

        Parameters
        ----------
        email : str
            Endereço de e-mail
        senha : str
            Senha do usuário
        
        Returns
        -------
        bool
            True se o usuário está cadastrado e a senha está correta, False caso contrário
        
        """
        cursor.execute(
            'SELECT * FROM Usuarios WHERE email = %s AND senha = %s', (email, senha))
        resultado = cursor.fetchone()
        if resultado == None:
            return True
        else:
            return False

    def cad_jogo(self, nome, fase, descri, dica):
        """ 
        Cadastra um novo jogo no banco de dados

        Parameters
        ----------
        nome : str
            Nome do jogo
        fase : str
            Fase do jogo
        descri : str
            Descrição do jogo
        dica : str
            Dica do jogo
        
        Returns
        -------
        bool
            True se o jogo foi cadastrado com sucesso, False caso contrário
        
        """
        cursor.execute('''INSERT INTO Jogos (nome,fase,descri,dica) VALUES (%s, %s, %s,%s)''',
                       (nome, fase, descri, dica))
        conexao.commit()
        return True

    def listar_jogos(self, nome):
        """
        Lista os dados de um jogo específico

        Parameters
        ----------
        nome : str
            Nome do jogo

        Returns
        -------
        list
            Lista com os dados do jogo
        bool
            True se o jogo foi encontrado, False caso contrário
            
        """
        cursor.execute('SELECT * FROM Jogos WHERE nome = %s', (nome,))
        resultado = cursor.fetchall()
        sucesso = bool(resultado)
        return resultado, sucesso

    def listar_clientes(self, email):
        """ 
        Lista os dados de um cliente específico

        Parameters
        ----------
        email : str
            Endereço de e-mail
        
        Returns
        -------
        list
            Lista com os dados do cliente
        bool
            True se o cliente foi encontrado, False caso contrário
        
        """
        cursor.execute('SELECT * FROM Usuarios WHERE email = %s', (email,))
        resultado = cursor.fetchone()
        return resultado

    def especifico(self, fase, nome):
        """ 
        Lista os dados de um jogo específico

        Parameters
        ----------
        fase : str
            Fase do jogo
        nome : str
            Nome do jogo
        
        Returns
        -------
        list
            Lista com os dados do jogo
        bool
            True se o jogo foi encontrado, False caso contrário
        
            
        """
        cursor.execute('SELECT * FROM jogos WHERE fase = %s AND nome = %s', (fase, nome))
        resultado = cursor.fetchall()
        sucesso = bool(resultado)
        return resultado, sucesso

    def new_jogos(self,nome):
        cursor.execute('INSERT INTO jogos (nome) VALUES (%s)',(nome,))
    

    
class MyThread(threading.Thread):
    """
    Classe para criar uma thread para cada cliente conectado
     Parameters
    ----------
    threading : Thread
        Classe para criar uma thread

    Methods
    -------
    run()
        Método para rodar a thread
    logar()
        Verifica se o usuário está cadastrado no banco de dados e se a senha está correta
    cadastrar()
        Cadastra um novo usuário no banco de dados
    cad_jogo()
        Cadastra um novo jogo no banco de dados
    listar_jogos()
        Lista os dados de um jogo específico
    listar_clientes()
        Lista os dados de um cliente específico
    especifico()
        Lista os dados de um jogo específico

    Returns
    -------
    None
        None

    
    """
    def __init__(self, client_address, client_socket):
        """ 
        Construtor da classe MyThread 

        Parameters
        ----------
        client_address : str
            Endereço do cliente
        client_socket : socket
            Socket do cliente
        
            
        Returns
        -------
        None
            None

        
        
        """
        threading.Thread.__init__(self)
        self.name = ''
        self.client_socket = client_socket
        print('Nova conexão, endereço:', client_address)

    def run(self):
        """
        Método para rodar a thread

        Methods
        -------
        logar()
            Verifica se o usuário está cadastrado no banco de dados e se a senha está correta
        cadastrar()
            Cadastra um novo usuário no banco de dados
        cad_jogo()
            Cadastra um novo jogo no banco de dados
        listar_jogos()
            Lista os dados de um jogo específico
        listar_clientes()
            Lista os dados de um cliente específico
        especifico()
            Lista os dados de um jogo específico


        Returns
        -------
        None
            None
            
        
        """
        con = self.client_socket
        metodos = Metodos()
        while True:
            try:
                msgLogin = con.recv(80000)
                mensagemStr = msgLogin.decode().split(',')

                enviar = ''
                if mensagemStr[0] == '1':
                    email = mensagemStr[1]
                    senha = mensagemStr[2]
                    print(f'O usuário {email} está tentando logar')
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
                    if metodos.cad_jogo(nome, ano_lancamento, descri, dica):
                        enviar = '1'
                    else:
                        enviar = '0'
                elif mensagemStr[0] == '4':
                    nome = mensagemStr[1]
                    print('Conectado 4')
                    resultado, sucesso = metodos.listar_jogos(nome)
                    if sucesso:
                        resul = json.dumps(resultado)  # Converter o objeto Python em uma string JSON
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
                

                elif mensagemStr[0] == '6':
                    fase = mensagemStr[1]
                    nome = mensagemStr[2]
                    print('Conectado 6')
                    resultado, sucesso = metodos.especifico(fase, nome)
                    if sucesso:
                        resul = json.dumps(resultado)  # Converter o objeto Python em uma string JSON
                        print(resul)
                        con.send(resul.encode())

                    else:
                        enviar = '0'

                elif mensagemStr[0] == '7':
                    nome = mensagemStr[1]
                    print('Conectado 7')
                    if metodos.new_jogos(nome):
                        enviar = '1'
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
    """ 
    Função principal do servidor

    Parameters
    ----------
    None

    Returns
    -------
    None
        None

    Exepction
    ---------
    Exception
        Erro ao processar a mensagem
    ConnectionResetError
        A conexão foi redefinida pelo cliente


    """
    metodos = Metodos()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip = ip_address
    #ip = '10.180.46.88'
    port = 8005
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
