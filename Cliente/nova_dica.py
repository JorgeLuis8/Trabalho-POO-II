# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'novas_dicas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class cad(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        MainWindow.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #D3D3D3);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 121, 601))
        self.frame.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #D3D3D3);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 81, 23))
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
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 60, 81, 23))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6 ;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 570, 75, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 91, 21))
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
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(20, 90, 75, 23))
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    background-color:  #AABAF2 ;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 100, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius: 10px;\n"
"background-color: transparent;\n"
"border: 2px solid black;\n"
"\n"
"")
        self.lineEdit_3.setMaxLength(2000000000)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 210, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 10px;\n"
"background-color: transparent;\n"
"border: 2px solid black;\n"
"\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 230, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.cad = QtWidgets.QPushButton(self.centralwidget)
        self.cad.setGeometry(QtCore.QRect(410, 390, 81, 23))
        self.cad.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.cad.setObjectName("cad")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 170, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
"background-color: transparent;\n"
"border: 2px solid black;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 70, 391, 22))
        self.comboBox.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid black;\n"
"background: transparent,white;\n"
"")
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/lol_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/valorant_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/The_Legend_of_Zelda_-_Ocarina_of_Time_29_icon.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/GtaV_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/gtasan_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/portal2_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Images/cuphead_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Images/undertale_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../Images/re3199_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../Images/Resident_evil_2_(2018)_logo_(cropped).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../Images/SILENT_HILL_2_LOGO_(Alt.).svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../Images/Shadow_of_the_Colossus_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../Images/eldenring_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../Images/Dead_Space_logo_(2023).svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../Images/png-transparent-hitman-iii-logo-red-games-hitman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon14, "")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../Images/re3_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon15, "")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../Images/clashofclans_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon16, "")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../Images/png-clipart-grand-theft-auto-vice-city-stories-grand-theft-auto-san-andreas-playstation-2-bully-gta-vice-city-avatar-text-logo-thumbnail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon17, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Perfil"))
        self.pushButton_5.setText(_translate("MainWindow", "Pesquisar Dicas"))
        self.pushButton_3.setText(_translate("MainWindow", "Deslogar"))
        self.pushButton_2.setText(_translate("MainWindow", "Novos Jogos"))
        self.pushButton_18.setText(_translate("MainWindow", "Cadastar Dicas"))
        self.label_3.setText(_translate("MainWindow", "Descrição"))
        self.label_2.setText(_translate("MainWindow", "Jogo"))
        self.label_4.setText(_translate("MainWindow", "Dica"))
        self.label.setText(_translate("MainWindow", "CADASTRE UMA DICA"))
        self.cad.setText(_translate("MainWindow", "Cadastrar Dica"))
        self.label_5.setText(_translate("MainWindow", "Fase:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "League of Legends"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Valorant"))
        self.comboBox.setItemText(2, _translate("MainWindow", "The Legend of Zelda: Ocarina of Time (1998)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Grand Theft Auto V"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Grand Thef Auto: San  Andreas"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Portal 2 (2011)"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Cuphead"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Undertale"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Resident Evil 3 (1999)"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Resident Evil 2 (Remake)"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Silent Hill 2"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Shadow of the Colossus"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Elden Ring"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Dead Space"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Hitman 3"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Resident Evil 3 (Remake)"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Clash of Clans"))
        self.comboBox.setItemText(17, _translate("MainWindow", "GTA:Vice City"))
