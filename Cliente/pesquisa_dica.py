# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesquisa_dica.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Pesquisa_dica(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 120, 601))
        self.frame.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #D3D3D3);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 81, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 81, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 80, 81, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color:  #AABAF2 ;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.voltar = QtWidgets.QPushButton(self.frame)
        self.voltar.setGeometry(QtCore.QRect(20, 570, 75, 23))
        self.voltar.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.voltar.setObjectName("voltar")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 150, 81, 23))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 110, 75, 23))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 170, 401, 341))
        self.plainTextEdit.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 60, 421, 22))
        self.comboBox.setStyleSheet("background-color: transparent;\n"
"border: 1px solid black;\n"
"background: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar Dicas"))
        self.pushButton_2.setText(_translate("MainWindow", "Perfil"))
        self.pushButton_3.setText(_translate("MainWindow", "Pesquisar Dicas"))
        self.voltar.setText(_translate("MainWindow", "Deslogar"))
        self.pushButton_6.setText(_translate("MainWindow", "Cadastrar Jogos"))
        self.label.setText(_translate("MainWindow", "ENCONTRE A DICA QUE DESEJA"))
        self.pushButton_4.setText(_translate("MainWindow", "Pesquisar"))
        self.label_2.setText(_translate("MainWindow", "Dicas"))
        self.comboBox.setItemText(0, _translate("MainWindow", "League of Legends"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Valorant"))
        self.comboBox.setItemText(2, _translate("MainWindow", "The Legend of Zelda: Ocarina of Time (1998)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Grand Theft Auto V"))
        self.comboBox.setItemText(4, _translate("MainWindow", "The Last of Us"))
        self.comboBox.setItemText(5, _translate("MainWindow", "God of War (2018)"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Grand Thef Auto: San  Andreas"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Portal 2 (2011)"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Cuphead"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Dota 2"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Undertale"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Resident Evil 3 (1999)"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Resident Evil 2 (Remake)"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Silent Hill 2"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Shadow of the Colossus"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Elden Ring"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Hades"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Lost Ark"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Legends of Runeterra"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Dead Space"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Overwatch 2"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Hitman 3"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Halo  Infinite"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Call of Duty: Warzone"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Resident Evil 3 (Remake)"))
