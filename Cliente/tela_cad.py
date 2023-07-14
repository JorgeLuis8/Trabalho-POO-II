# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cad.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_cad(object):
    """
        Classe que cria a tela de cadastro de jogos

        Methods
        -------
        setupUi(MainWindow)
                Cria todos os elementos da tela de cadastro de jogos

        retranslateUi(MainWindow)
                Coloca textos nos elementos da tela de cadastro de jogos

    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 557)
        MainWindow.setMinimumSize(QtCore.QSize(803, 557))
        MainWindow.setMaximumSize(QtCore.QSize(803, 557))
        MainWindow.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #D3D3D3);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Botao_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_voltar.setGeometry(QtCore.QRect(0, 530, 75, 23))
        self.Botao_voltar.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.Botao_voltar.setObjectName("Botao_voltar")
        self.Botao_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_cadastrar.setGeometry(QtCore.QRect(340, 270, 75, 23))
        self.Botao_cadastrar.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.Botao_cadastrar.setObjectName("Botao_cadastrar")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 90, 400, 20))
        self.lineEdit_3.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 31, 20))
        self.label_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 110, 400, 20))
        self.lineEdit_4.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 110, 31, 27))
        self.label_6.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 401, 20))
        self.lineEdit.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 101, 20))
        self.label_4.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 150, 401, 20))
        self.lineEdit_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 150, 21, 20))
        self.label_3.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 170, 31, 21))
        self.label_5.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 170, 401, 20))
        self.lineEdit_5.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastro"))
        self.Botao_voltar.setText(_translate("MainWindow", " <-- Voltar"))
        self.Botao_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "ano/mes/dia"))
        self.label_4.setText(_translate("MainWindow", "Data de nascimento"))
        self.label_3.setText(_translate("MainWindow", "User"))
        self.label_5.setText(_translate("MainWindow", "Senha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_cad()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
