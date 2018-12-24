# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.amigosWidget = QtWidgets.QListWidget(self.centralwidget)
        self.amigosWidget.setGeometry(QtCore.QRect(10, 30, 101, 401))
        self.amigosWidget.setObjectName("amigosWidget")
        self.notificarButton = QtWidgets.QPushButton(self.centralwidget)
        self.notificarButton.setGeometry(QtCore.QRect(590, 440, 75, 23))
        self.notificarButton.setObjectName("notificarButton")
        self.textoEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textoEdit.setGeometry(QtCore.QRect(130, 390, 451, 71))
        self.textoEdit.setObjectName("textoEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 440, 101, 23))
        self.addButton.setObjectName("addButton")
        self.enviarButton = QtWidgets.QPushButton(self.centralwidget)
        self.enviarButton.setGeometry(QtCore.QRect(590, 390, 75, 41))
        self.enviarButton.setObjectName("enviarButton")
        self.amigosLabel = QtWidgets.QLabel(self.centralwidget)
        self.amigosLabel.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.amigosLabel.setObjectName("amigosLabel")
        self.mengagemLabel = QtWidgets.QLabel(self.centralwidget)
        self.mengagemLabel.setGeometry(QtCore.QRect(130, 10, 191, 16))
        self.mengagemLabel.setObjectName("mengagemLabel")
        self.textoLabel = QtWidgets.QLabel(self.centralwidget)
        self.textoLabel.setGeometry(QtCore.QRect(130, 370, 201, 16))
        self.textoLabel.setObjectName("textoLabel")
        self.messagensListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.messagensListWidget.setGeometry(QtCore.QRect(130, 30, 521, 331))
        self.messagensListWidget.setWordWrap(True)
        self.messagensListWidget.setObjectName("messagensListWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat - Programação em Tempo Real"))
        self.notificarButton.setText(_translate("MainWindow", "Notificar"))
        self.addButton.setText(_translate("MainWindow", "Adicionar"))
        self.enviarButton.setText(_translate("MainWindow", "Enviar"))
        self.amigosLabel.setText(_translate("MainWindow", "Amigos"))
        self.mengagemLabel.setText(_translate("MainWindow", "<html><head/><body><p>Mensagem</p></body></html>"))
        self.textoLabel.setText(_translate("MainWindow", "Texto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

