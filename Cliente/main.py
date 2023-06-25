import sys
import os
import socket

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaInicio import Tela_inical
from tela_cad import Tela_cad
from telaAbout import About_us
from home import Tela_home
from cad_jogos import Tela_jogos

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

        self.tela_inical = Tela_inical()
        self.tela_inical.setupUi(self.stack0)

        self.tela_cadastro = Tela_cad()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_about = About_us()
        self.tela_about.setupUi(self.stack2)

        self.tela_home = Tela_home()
        self.tela_home.setupUi(self.stack3)

        self.tela_jogos = Tela_jogos()
        self.tela_jogos.setupUi(self.stack4)

        self.Qstack.addWidget(self.stack0)
        self.Qstack.addWidget(self.stack1)
        self.Qstack.addWidget(self.stack2)
        self.Qstack.addWidget(self.stack3)
        self.Qstack.addWidget(self.stack4)


class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)


        ip = 'localhost'
        port = 8088
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
        self.tela_home.voltar.clicked.connect(self.voltar)
        self.tela_home.pushButton.clicked.connect(self.ir_jogos)
        self.tela_jogos.pushButton.clicked.connect(self.cadastrar_jogos)
    def serverCadastro(self, msgCad):
        if msgCad.split(',')[0] == '2':
            self.client_socket.send(msgCad.encode())
            msg = self.client_socket.recv(1024).decode()

            if msg == '1':
                return True
        return False

    def cadastro(self):
        nome = self.tela_cadastro.lineEdit_3.text()
        email = self.tela_cadastro.lineEdit_4.text()
        endereco = self.tela_cadastro.lineEdit.text()
        user = self.tela_cadastro.lineEdit_2.text()
        senha = self.tela_cadastro.lineEdit_5.text()

        if nome and email and senha and endereco and user:
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
           
    def login(self):
        email = self.tela_inical.campoUsuario.text()  
        senha = self.tela_inical.campoSenha.text()
        msgLogin = f'1,{email},{senha}'
        if not (email == None or senha == None or email == '' or senha == ''):
            print('entrou aqui')
            if not self.serverLogin(msgLogin):
                self.tela_inical.campoUsuario.clear()
                self.tela_inical.campoSenha.clear()
                self.Qstack.setCurrentIndex(3)
                QMessageBox.information(None, 'Sucesso', 'Login realizado com sucesso')
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
        nome = self.tela_jogos.lineEdit.text()
        data = self.tela_jogos.lineEdit_2.text()
        descricao = self.tela_jogos.lineEdit_3.text()
        dica = self.tela_jogos.lineEdit_4.text()
        msgCad = f'3,{nome},{data},{descricao},{dica}'
        if not (nome == None and data == None and descricao == None and dica == None and nome == '' and data == '' and descricao == '' and dica == ''):
            if self.serverCadjogos(msgCad):
                self.tela_jogos.lineEdit.clear()
                self.tela_jogos.lineEdit_2.clear()
                self.tela_jogos.lineEdit_3.clear()
                self.tela_jogos.lineEdit_4.clear()
                QMessageBox.information(None, 'Sucesso', 'Cadastro realizado com sucesso')
        else:
            QMessageBox.information(None, 'Atenção', 'Preencha todos os campos')
          
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
