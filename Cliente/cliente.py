import sys
import os
import socket
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap

from tela_Inicio import Tela_inical
from tela_cad import Tela_cad
from telaAbout import About_us
from home import Tela_home
from novo_jogo import Cadastro_jogos
from pesquisa_dica import Pesquisa_dica
from nova_dica import cad
import configparser


class Ui_main(QtWidgets.QWidget):
    """ 
    Classe que define a interface gráfica da tela principal do programa.

    Methods
    -------
    setupUi(Main)
            Cria todos os elementos da tela principal

    retranslateUi(Main)
            Coloca textos nos elementos da tela principal
    
    
    Parameters
    ----------
    QMainWindow
            Classe que cria a tela principal do programa

    



    
    """
    def setupUi(self, Main):

        """
        Cria todos os elementos da tela principal

        Parameters
        ----------
        Main
                Classe que cria a tela principal do programa

        Methods
        -------
        setupUi(Main)
                Cria todos os elementos da tela principal

        retranslateUi(Main)
                Coloca textos nos elementos da tela principal

        

        """
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.Qstack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_inical = Tela_inical()
        self.tela_inical.setupUi(self.stack0)

        self.tela_cadastro = Tela_cad()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_about = About_us()
        self.tela_about.setupUi(self.stack2)

        self.tela_home = Tela_home()
        self.tela_home.setupUi(self.stack3)

        self.tela_jogos = cad()
        self.tela_jogos.setupUi(self.stack4)

        self.tela_dica = Pesquisa_dica()
        self.tela_dica.setupUi(self.stack5)

        self.cadastro_jogos = Cadastro_jogos()
        self.cadastro_jogos.setupUi(self.stack6)

        self.Qstack.addWidget(self.stack0)
        self.Qstack.addWidget(self.stack1)
        self.Qstack.addWidget(self.stack2)
        self.Qstack.addWidget(self.stack3)
        self.Qstack.addWidget(self.stack4)
        self.Qstack.addWidget(self.stack5)
        self.Qstack.addWidget(self.stack6)


class Main(QMainWindow, Ui_main):
    """
    Cria a tela principal do programa e define as funções de cada botão.

    Methods
    -------
    sair()
            Fecha o programa

    Tela_sobre()
            Vai para a tela sobre

    Tela_cad()
            Vai para a tela de cadastro

    login()
            Faz o login do usuário

    voltar()
            Volta para a tela inicial

    cadastro()
            Cadastra um novo usuário

    dica()
            Vai para a tela de pesquisa de dicas

    ir_jogos()
            Vai para a tela de cadastro de jogos

    cad_jogos()
            Vai para a tela de cadastro de jogos
            
    cadastrar_jogos()
            Cadastra um novo jogo
        
    voltar2()
            Volta para a tela home

    Parameters
    ----------
    QMainWindow
            Classe que cria a tela principal do programa

    Ui_main
            Classe que define a interface gráfica da tela principal do programa


    Returns
    -------
    None
            A função não retorna nada, apenas executa as ações necessárias


        
    """
    def __init__(self, parent=None):
        """
        Cria a tela principal do programa e define as funções de cada botão.

        Parameters
        ----------
        QMainWindow
                Classe que cria a tela principal do programa

        Ui_main
                Classe que define a interface gráfica da tela principal do programa

            
        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias


        """
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.usuario_logado = None
        self.jogos_cadastrados = []
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ip = ip_address
        #ip ='10.180.46.88'
        port = 8005
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr) 

        self.tela_inical.Botao_sair.clicked.connect(self.sair)
        self.tela_inical.Botao_sobre.clicked.connect(self.Tela_sobre)
        self.tela_inical.botaoCadastro.clicked.connect(self.Tela_cad)
        self.tela_inical.botaoLogin.clicked.connect(self.login)

        self.tela_cadastro.Botao_voltar.clicked.connect(self.voltar)
        self.tela_cadastro.Botao_cadastrar.clicked.connect(self.cadastro)

        self.tela_about.pushButton.clicked.connect(self.voltar)

        
        self.tela_home.pushButton_3.clicked.connect(self.dica) #pesquisa dicas
        self.tela_home.pushButton_6.clicked.connect(self.ir_jogos) #cadastra novas dicas
        self.tela_home.voltar.clicked.connect(self.voltar)
        self.tela_home.pushButton.clicked.connect(self.cad_jogos) #cadastra novos jogos
        


        self.tela_jogos.pushButton_4.clicked.connect(self.voltar2) #volta para tela home
        self.tela_jogos.pushButton_5.clicked.connect(self.dica) # tela de Pesquisa dicas
        self.tela_jogos.pushButton_2.clicked.connect(self.cad_jogos) #cadastra novos jogs
        self.tela_jogos.cad.clicked.connect(self.cadastrar_jogos) #cadastra novos jogos
        self.tela_jogos.pushButton_3.clicked.connect(self.voltar)# desloga
        

        self.tela_dica.pushButton_2.clicked.connect(self.voltar2) #volta para tela home
        self.tela_dica.pushButton_6.clicked.connect(self.ir_jogos) #cadastra novas dicas
        self.tela_dica.pushButton.clicked.connect(self.cad_jogos) #cadastra novos jogos
        self.tela_dica.pushButton_4.clicked.connect(self.dicas) #pesquisa a dica
        self.tela_dica.pushButton_5.clicked.connect(self.pesquisa_especifica) #pesquisa a dica especifica
        self.tela_dica.voltar.clicked.connect(self.voltar) #desloga
        


        self.cadastro_jogos.pushButton_4.clicked.connect(self.voltar2) #volta para tela home
        self.cadastro_jogos.pushButton_5.clicked.connect(self.dica) # tela de Pesquisa dicas
        self.cadastro_jogos.pushButton_2.clicked.connect(self.ir_jogos) #cadastra novas dicas
        self.cadastro_jogos.pushButton_3.clicked.connect(self.voltar)
        self.cadastro_jogos.pushButton.clicked.connect(self.new_joos) #cadastra novos jogos
        #self.cadastro_jogos.pushButton_6.clicked.connect(self.img)
        self.preencher_combobox_jogos()
    #Faz a comunicação com o servidor para verficar o cadastro.
    def serverCadastro(self, msgCad):
        """
        Faz a comunicação com o servidor para verficar o cadastro.

        Parameters
        ----------
        msgCad : str
                String que contém os dados do usuário que está sendo cadastrado


        Returns
        -------
        bool
                Retorna True se o cadastro foi realizado com sucesso e False caso contrário


        """
        help(self.serverCadastro)

        if msgCad.split(',')[0] == '2':
            self.client_socket.send(msgCad.encode())
            msg = self.client_socket.recv(1024).decode()

            if msg == '1':
                return True
            else:
                return False
    #Cadastro de usuario no sistema, verifica se os campos estão preenchidos e se não existem email e usuarios iguais ja cadastrodos no sistema.
    def cadastro(self):
        """
        Cadastro de usuario no sistema, verifica se os campos estão preenchidos e se não existem email e usuarios iguais ja cadastrodos no sistema.

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias
        """
        help(self.cadastro)
        nome = self.tela_cadastro.lineEdit_3.text()
        email = self.tela_cadastro.lineEdit_4.text()
        endereco = self.tela_cadastro.lineEdit.text()
        user = self.tela_cadastro.lineEdit_2.text()
        senha = self.tela_cadastro.lineEdit_5.text()
        if not (nome == None or email == None or endereco == None or user == None or senha == None or nome == '' or email == '' or endereco == '' or user == '' or senha == ''):
            msgCad = f'2,{nome},{email},{endereco},{user},{senha}'
            if self.serverCadastro(msgCad):
                self.tela_cadastro.lineEdit.clear()
                self.tela_cadastro.lineEdit_2.clear()
                self.tela_cadastro.lineEdit_3.clear()
                self.tela_cadastro.lineEdit_4.clear()
                self.tela_cadastro.lineEdit_5.clear()
                QMessageBox.information(None, 'Sucesso', 'Cadastro realizado com sucesso')
            else:
                    QMessageBox.information(None, 'Atenção', 'Email ou usuário já cadastrados')
                    self.tela_cadastro.lineEdit.clear()
                    self.tela_cadastro.lineEdit_2.clear()
                    self.tela_cadastro.lineEdit_3.clear()
                    self.tela_cadastro.lineEdit_4.clear()
                    self.tela_cadastro.lineEdit_5.clear()
        else:
                QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')
    #faz a comunicação com o servidor, para fazer o login.           
    def serverLogin(self, msgLogin):
        """
        Faz a comunicação com o servidor, para fazer o login.

        Parameters
        ----------
        msgLogin : str
                String que contém os dados do usuário que está fazendo o login


        Returns
        -------
        bool
                Retorna True se o login foi realizado com sucesso e False caso contrário
        """
        if  msgLogin.split(',')[0] == '1':
            self.client_socket.send(msgLogin.encode())
            msg = self.client_socket.recv(1024).decode()
            if msg and msg == '1' :
                return True
            else:
                return False
        return msg
    #Seta as informações dos usuarios logados na tela inical 
    def serverinfo(self,msgInfo):
        """
        Seta as informações dos usuarios logados na tela inical

        Parameters
        ----------
        msgInfo : str
                String que contém os dados do usuário que está fazendo o login


        Returns
        -------
        list
                Retorna uma lista com os dados do usuário que está fazendo o login


        """
        if msgInfo.split(',')[0] == '5':
            self.client_socket.send(msgInfo.encode())
            msg = self.client_socket.recv(1024).decode().split(',')
            return msg
        
    def login(self):
        """
        Faz o login do usuário no sistema, verificando se os campos estão preenchidos e se o usuário existe no sistema

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias
        """
        email = self.tela_inical.campoUsuario.text()  
        senha = self.tela_inical.campoSenha.text()
        msgLogin = f'1,{email},{senha}'
        if not (email == None or senha == None or email == '' or senha == ''):
            print('entrou aqui')
            if  self.serverLogin(msgLogin):
                self.tela_inical.campoUsuario.clear()
                self.tela_inical.campoSenha.clear()
                self.Qstack.setCurrentIndex(3)
                msgInfo = f'5,{email}'
                self.serverinfo (msgInfo)
                resultado = self.serverinfo(msgInfo)

                self.tela_home.lineEdit.setText(resultado[1].replace("'", " "))
                self.tela_home.lineEdit_2.setText(resultado[6].replace("'", " "))
                self.tela_home.lineEdit_3.setText(resultado[2].replace("'", " "))
                self.usuario_logado = resultado[1].replace("'", " ")

            else:
                QMessageBox.information(None, 'Atenção', 'Email ou senha incorretos')
        else:
            QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')
          
    def serverCadjogos(self, msgCadJogos):
        """
        Faz a comunicação com o servidor, para cadastrar os jogos.

        Parameters
        ----------
        msgCadJogos : str
                String que contém os dados do jogo que está sendo cadastrado


        Returns
        -------
        bool
                Retorna True se o cadastro foi realizado com sucesso e False caso contrário

        """
        if msgCadJogos.split(',')[0] == '3':
            self.client_socket.send(msgCadJogos.encode())
            msg = self.client_socket.recv(1024).decode()

            if msg and msg == '1':
                return True
            else:
                return False

    def cadastrar_jogos(self):
        """
        Cadastra os jogos no sistema, verificando se os campos estão preenchidos e se o jogo já existe no sistema

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias

                
        """
        nome = self.tela_jogos.comboBox.currentText()
        data = self.tela_jogos.lineEdit_2.text()
        descricao = self.tela_jogos.lineEdit_3.text()
        dica = self.tela_jogos.lineEdit_4.text()
        msgCad = f'3,{nome},{data},{descricao},{dica}'
        print(msgCad)
        if not (nome == None or data == None or descricao == None or dica == None or nome == '' or data == '' or descricao == '' or dica == ''):
            print('entrou no cad')
            if self.serverCadjogos(msgCad):
                self.tela_jogos.lineEdit_2.clear()
                self.tela_jogos.lineEdit_3.clear()
                self.tela_jogos.lineEdit_4.clear()

                QMessageBox.information(None, 'Sucesso', 'Cadastro realizado com sucesso')
            else:
                QMessageBox.information(None, 'Atenção', 'Erro ao cadastrar')
        else:
            QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')

            
    def serverDica(self, nome):
        """
        Faz a comunicação com o servidor, para pegar as dicas.

        Parameters
        ----------
        nome : str
                String que contém o nome do jogo que está sendo pesquisado


        Returns
        -------
        list
                Retorna uma lista com as dicas do jogo que está sendo pesquisado    


        """
        if nome:
            while True:
                msgDica = f'4,{nome}'
                self.client_socket.send(msgDica.encode())
                data = self.client_socket.recv(80000).decode()

                try:
                    msg = json.loads(data) 
                    print(msg) # Converter a string JSON em um objeto Python
                    return msg
                except json.decoder.JSONDecodeError as e:
                    print(f"Erro na decodificação JSON: {e}")
                    return None
        return None


    def dicas(self):
        """
        Pega as dicas do jogo selecionado, verificando se o jogo foi selecionado

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias

        """
        nome = self.tela_dica.comboBox.currentText()
        self.tela_dica.plainTextEdit.clear()  # Limpa o conteúdo anterior
        self.tela_dica.plainTextEdit_2.clear()  # Limpa o conteúdo anterior
        self.tela_dica.lineEdit.clear()  # Limpa o conteúdo anterior
        if nome:
            self.tela_dica.plainTextEdit.clear()  # Limpa o conteúdo anterior
            resultado = self.serverDica(nome)

            if resultado is not None and isinstance(resultado, list):
                if resultado and resultado[0] == '0':
                    QMessageBox.information(None, 'Atenção', 'Dica não cadastrada no sistema')
                else:
                    for item in resultado:
                        if len(item) == 5:  # Verifica se o item tem o número esperado de elementos
                            id_jogo, nome, fase, descricao, dica = item
                            texto = f"Fase: {fase}\nDescrição: {descricao}\nDica: {dica}\n\n"
                            self.tela_dica.plainTextEdit.appendPlainText(texto)
                        else:
                            print(f"Item inválido: {item}")

                    if not resultado:
                        QMessageBox.information(None, 'Atenção', 'Dica não cadastrada no sistema')
            else:
                QMessageBox.information(None, 'Atenção', 'Dica não cadastrada no sistema')
        else:
            QMessageBox.information(None, 'Atenção', 'Selecione um jogo')

 

    def serverEspec(self, fase,nome):
        """
        Faz a comunicação com o servidor, para pegar as dicas de um jogo em especifico.

        Parameters
        ----------
        fase : str
                String que contém a fase do jogo que está sendo pesquisado
        nome : str
                String que contém o nome do jogo que está sendo pesquisado

                
        Returns
        -------
        list
                Retorna uma lista com as dicas do jogo que está sendo pesquisado


        """
        if nome:
            while True:
                msgDica = f'6,{fase},{nome}'
                self.client_socket.send(msgDica.encode())
                data = self.client_socket.recv(1024).decode()
                try:
                    msg = json.loads(data) 
                    print(msg) # Converter a string JSON em um objeto Python
                    return msg
                except json.decoder.JSONDecodeError as e:
                    print(f"Erro na decodificação JSON: {e}")
                    return None
        return None


    def pesquisa_especifica(self):
        """
        Pega as dicas do jogo selecionado, verificando se o jogo foi selecionado

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias


        """
        fase = self.tela_dica.lineEdit.text()
        nome = self.tela_dica.comboBox.currentText()
        self.tela_dica.plainTextEdit_2.clear()  
        
        results = self.serverEspec(fase, nome)
        if not nome == '' or nome == None or fase == '' or fase == None:
            if results:
                for result in results:
                    id_jogo, nome, fase, descricao, dica = result
                    texto = f"Fase: {fase}\nDescrição: {descricao}\nDica: {dica}\n\n"
                    self.tela_dica.plainTextEdit_2.appendPlainText(texto)
            else:
                QMessageBox.information(None, 'Atenção', 'Nenhuma dica encontrada para o jogo e fase especificados')
        else:
            QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')
    
    def serverNJogos(self,msg):
        """
        Faz a comunicação com o servidor, para cadastrar um novo jogo.

        Parameters
        ----------
        msg : str
                String que contém o nome do jogo que está sendo cadastrado


        Returns
        -------
        bool
                Retorna True se o cadastro foi realizado com sucesso, e False caso contrário
                

        """
        if msg.split(',')[0] == '7':
            self.client_socket.send(msg.encode())
            msg = self.client_socket.recv(1024).decode()

            if msg and msg == '1':
                return True
            else:
                return False
            
    def new_joos(self):
        """
        Cadastra um novo jogo, verificando se o nome do jogo foi preenchido

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias


        """
        nome = self.cadastro_jogos.lineEdit.text()
        msgCad = f'7,{nome}'
     
        if not (nome == None or nome == ''):
            if self.serverNJogos(msgCad):
                self.cadastro_jogos.lineEdit.clear()
                QMessageBox.information(None, 'Sucesso', 'Cadastro realizado com sucesso')
                self.preencher_combobox_jogos()
            else:
                QMessageBox.information(None, 'Atenção', 'Erro ao cadastrar')
        else:
            QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')


    def recebeJogos(self, msgj):
       """
         Faz a comunicação com o servidor, para receber os jogos cadastrados.

        Parameters
        ----------
        msgj : str
                String que contém o nome do jogo que está sendo pesquisado


        Returns
        -------
        list
                Retorna uma lista com os jogos cadastrados no sistema


       """
       if msgj.split(',')[0] == '8':
            self.client_socket.send(msgj.encode())
            msg = self.client_socket.recv(1024).decode().split(',')
            return msg
        
    def preencher_combobox_jogos(self):
        """
        Preenche o combobox de jogos, com os jogos cadastrados no sistema

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias

        """
        nome = self.cadastro_jogos.lineEdit.text()
        msgInfo = f'8,{nome}'
        lista_jogos = self.recebeJogos(msgInfo)
        image_path = self.cadastro_jogos.lineEdit_2.text()
        icon = QIcon(image_path)
        index = self.tela_dica.comboBox.count() - 1

        if lista_jogos[0] != 0:
                lista_jogos_limpa = [item.replace("[", "").replace("]", "").replace("'", "").strip() for item in lista_jogos]

                for jogo in lista_jogos_limpa:
                        if self.tela_dica.comboBox.findText(jogo) == -1:
                                self.tela_dica.comboBox.addItem(jogo)
                                self.tela_dica.comboBox.setItemIcon(index,icon)
                        if self.tela_jogos.comboBox.findText(jogo) == -1:
                                self.tela_jogos.comboBox.addItem(jogo)
                                self.tela_jogos.comboBox.setItemIcon(index,icon)
        else:
                return 0
        

    def voltar(self):
        """
        Volta para a tela inicial

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias
        """
        self.Qstack.setCurrentIndex(0)

    def Tela_cad(self):
        """
        Vai para a tela de cadastro

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias
        """
        self.Qstack.setCurrentIndex(1)

    def Tela_sobre(self):
        """
        Vai para a tela de sobre

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias



        """
        self.Qstack.setCurrentIndex(2)

    def sair(self):
        """
        Sai do programa

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias


        """
        exit()

    def ir_jogos(self):
        """
        Vai para a tela de jogos

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias

        """
        self.Qstack.setCurrentIndex(4)

    def voltar2(self):
        """
        Volta para a tela inicial

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias
        """
        self.Qstack.setCurrentIndex(3)

    def dica(self):
        """
        Vai para a tela de dicas

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias


        """
        self.Qstack.setCurrentIndex(5)

    def cad_jogos(self):
        """
        Vai para a tela de cadastro de jogos

        Parameters
        ----------
        None

        Returns
        -------
        None
                A função não retorna nada, apenas executa as ações necessárias

        """
        self.Qstack.setCurrentIndex(6)


if __name__ == '__main__':
    """
    Função principal que inicia o programa

    Parameters
    ----------
    None

    Returns
    -------
    None
            A função não retorna nada, apenas executa as ações necessárias
    """
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())