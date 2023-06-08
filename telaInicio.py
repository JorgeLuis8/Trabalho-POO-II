# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_inical(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 565)
        MainWindow.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #D3D3D3);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"border: none;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.botaoLogin = QtWidgets.QPushButton(self.centralwidget)
        self.botaoLogin.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.botaoLogin.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.botaoLogin.setObjectName("botaoLogin")
        self.botaoCadastro = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastro.setGeometry(QtCore.QRect(360, 250, 75, 23))
        self.botaoCadastro.setMouseTracking(True)
        self.botaoCadastro.setTabletTracking(True)
        self.botaoCadastro.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.botaoCadastro.setAutoDefault(False)
        self.botaoCadastro.setDefault(False)
        self.botaoCadastro.setFlat(False)
        self.botaoCadastro.setObjectName("botaoCadastro")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 230, 271, 20))
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setAcceptDrops(False)
        self.label_5.setToolTipDuration(-1)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color:black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setLineWidth(1)
        self.label_5.setText("Ainda não possui uma conta? Cadastre-se clicando aqui:")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.Botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_sair.setGeometry(QtCore.QRect(10, 500, 75, 23))
        self.Botao_sair.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.Botao_sair.setObjectName("Botao_sair")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 100, 459, 13))
        self.label.setStyleSheet("color:black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.campoUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.campoUsuario.setGeometry(QtCore.QRect(170, 120, 459, 20))
        self.campoUsuario.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.campoUsuario.setObjectName("campoUsuario")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 140, 121, 21))
        self.label_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.campoSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.campoSenha.setGeometry(QtCore.QRect(170, 160, 459, 20))
        self.campoSenha.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.campoSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campoSenha.setObjectName("campoSenha")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 490, 204, 23))
        self.label_6.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_6.setObjectName("label_6")
        self.Botao_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_sobre.setGeometry(QtCore.QRect(720, 490, 81, 23))
        self.Botao_sobre.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.Botao_sobre.setObjectName("Botao_sobre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "Tela Inicial"))
        self.botaoLogin.setText(_translate("MainWindow", "Login"))
        self.botaoCadastro.setText(_translate("MainWindow", "Cadastro"))
        self.Botao_sair.setText(_translate("MainWindow", "Sair!"))
        self.label.setText(_translate("MainWindow", "Usuário/Email"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.label_6.setText(_translate("MainWindow", "Deseja saber mais sobre nós? Clique aqui: "))
        self.Botao_sobre.setText(_translate("MainWindow", "Sobre nós"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_inical()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
