import sys
import os
import socket
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaInicio import Tela_inical
from tela_cad import Tela_cad
from telaAbout import About_us
from home import Tela_home
from novo_jogo import Cadastro_jogos
from pesquisa_dica import Pesquisa_dica
from nova_dica import Cadastro_dicas

class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
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

        self.tela_jogos = Cadastro_jogos()
        self.tela_jogos.setupUi(self.stack4)

        self.tela_dica = Pesquisa_dica()
        self.tela_dica.setupUi(self.stack5)

        self.cadastro_jogos = Cadastro_dicas()
        self.cadastro_jogos.setupUi(self.stack6)

        self.Qstack.addWidget(self.stack0)
        self.Qstack.addWidget(self.stack1)
        self.Qstack.addWidget(self.stack2)
        self.Qstack.addWidget(self.stack3)
        self.Qstack.addWidget(self.stack4)
        self.Qstack.addWidget(self.stack5)
        self.Qstack.addWidget(self.stack6)


class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.usuario_logado = None
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ip = ip_address
        port = 8004
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

        
        self.tela_home.pushButton_6.clicked.connect(self.cad_jogos)
        self.tela_home.pushButton_3.clicked.connect(self.dica)
        self.tela_home.voltar.clicked.connect(self.voltar)
        self.tela_home.pushButton_6.clicked.connect(self.cad_jogos)
        self.tela_home.pushButton.clicked.connect(self.ir_jogos)
        


        self.tela_jogos.pushButton_3.clicked.connect(self.voltar) #deslogar
        self.tela_jogos.pushButton_4.clicked.connect(self.voltar2) # volar para tela home
        self.tela_jogos.pushButton_5.clicked.connect(self.dica) #tela de dicas
        self.tela_jogos.pushButton_2.clicked.connect(self.cad_jogos) #tela de cadastro de dica
        self.tela_jogos.pushButton.clicked.connect(self.ir_jogos) #tela de jogos
   
        self.tela_dica.pushButton_2.clicked.connect(self.voltar2) 
        self.tela_dica.pushButton_4.clicked.connect(self.dicas)
        self.tela_dica.voltar.clicked.connect(self.voltar)
        self.tela_dica.pushButton_6.clicked.connect(self.cad_jogos)
        self.tela_dica.pushButton.clicked.connect(self.ir_jogos)
        


        self.cadastro_jogos.pushButton_4.clicked.connect(self.voltar2)
        self.cadastro_jogos.pushButton_3.clicked.connect(self.voltar)
        #self.cadastro_jogos.pushButton.clicked.connect(self.cadastrar_jogos)
        self.cadastro_jogos.pushButton_5.clicked.connect(self.dica)
        self.cadastro_jogos.pushButton.clicked.connect(self.cad_jogos)
        


    def serverCadastro(self, msgCad):
        if msgCad.split(',')[0] == '2':
            self.client_socket.send(msgCad.encode())
            msg = self.client_socket.recv(1024).decode()

            if msg == '1':
                return True
            else:
                return False
    def cadastro(self):
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
                
    def serverLogin(self, msgLogin):
        if msgLogin.split(',')[0] == '1':
            self.client_socket.send(msgLogin.encode())
            msg = self.client_socket.recv(1024).decode()
            if msg and msg == '1' :
                return True
            else:
                return False
        return msg
    
    def serverinfo(self,msgInfo):
        if msgInfo.split(',')[0] == '5':
            self.client_socket.send(msgInfo.encode())
            msg = self.client_socket.recv(1024).decode().split(',')
            return msg
        
    def login(self):
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
        if msgCadJogos.split(',')[0] == '3':
            self.client_socket.send(msgCadJogos.encode())
            msg = self.client_socket.recv(1024).decode()

            if msg and msg == '1' :
                return True
            else:
                return False

    def cadastrar_jogos(self):
        nome = self.cadastro_jogos.lineEdit_5.text()
        data = self.cadastro_jogos.lineEdit_2.text()
        descricao = self.cadastro_jogos.lineEdit_3.text()
        dica = self.cadastro_jogos.lineEdit_4.text()
        msgCad = f'3,{nome},{data},{descricao},{dica}'
        print(msgCad)
        if not (nome == None or data == None or descricao == None or dica == None or nome == '' or data == '' or descricao == '' or dica == ''):
            print('entrou no cad')
            if self.serverCadjogos(msgCad):

                self.cadastro_jogos.lineEdit_5.clear()
                self.cadastro_jogos.lineEdit_2.clear()
                self.cadastro_jogos.lineEdit_3.clear()
                self.cadastro_jogos.lineEdit_4.clear()

                QMessageBox.information(None, 'Sucesso', 'Cadastro realizado com sucesso')
            else:
                QMessageBox.information(None, 'Atenção', 'Erro ao cadastrar')
        else:
            QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')
            
    def serverDica(self, nome):
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
        nome = self.tela_dica.comboBox.currentText()
        if nome:
            self.tela_dica.plainTextEdit.clear()  # Limpa o conteúdo anterior
            resultado = self.serverDica(nome)

            if resultado is not None and isinstance(resultado, list):
                if resultado and resultado[0] == '0':
                    QMessageBox.information(None, 'Atenção', 'Dica não cadastrada no sistema')
                else:
                    for item in resultado:
                        if len(item) == 5:  # Verifica se o item tem o número esperado de elementos
                            id_jogo, nome, data, descricao, dica = item
                            texto = f"Data de Lançamento: {data}\nDescrição: {descricao}\nDica: {dica}\n\n"
                            self.tela_dica.plainTextEdit.appendPlainText(texto)
                        else:
                            print(f"Item inválido: {item}")

                    if not resultado:
                        QMessageBox.information(None, 'Atenção', 'Dica não cadastrada no sistema')
            else:
                QMessageBox.information(None, 'Atenção', 'Dica não cadastrada no sistema')
        else:
            QMessageBox.information(None, 'Atenção', 'Selecione um jogo')

    def novos_jogos(self):
        pass

    def voltar(self):
        self.Qstack.setCurrentIndex(0)

    def Tela_cad(self):
        self.Qstack.setCurrentIndex(1)

    def Tela_sobre(self):
        self.Qstack.setCurrentIndex(2)

    def sair(self):
        exit()

    def ir_jogos(self):
        self.Qstack.setCurrentIndex(4)

    def voltar2(self):
        self.Qstack.setCurrentIndex(3)

    def dica(self):
        self.Qstack.setCurrentIndex(5)

    def cad_jogos(self):
        self.Qstack.setCurrentIndex(6)
  
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
