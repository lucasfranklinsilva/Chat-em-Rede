# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addDialog(object):
    def setupUi(self, addDialog):
        addDialog.setObjectName("addDialog")
        addDialog.resize(278, 133)
        self.nomeEdit = QtWidgets.QLineEdit(addDialog)
        self.nomeEdit.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.nomeEdit.setObjectName("nomeEdit")
        self.ipEdit = QtWidgets.QLineEdit(addDialog)
        self.ipEdit.setGeometry(QtCore.QRect(10, 80, 171, 20))
        self.ipEdit.setObjectName("ipEdit")
        self.salvarButton = QtWidgets.QPushButton(addDialog)
        self.salvarButton.setGeometry(QtCore.QRect(190, 30, 75, 31))
        self.salvarButton.setObjectName("salvarButton")
        self.fecharButton = QtWidgets.QPushButton(addDialog)
        self.fecharButton.setGeometry(QtCore.QRect(190, 70, 75, 31))
        self.fecharButton.setObjectName("fecharButton")
        self.nomeLabel = QtWidgets.QLabel(addDialog)
        self.nomeLabel.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.nomeLabel.setObjectName("nomeLabel")
        self.ipLabel = QtWidgets.QLabel(addDialog)
        self.ipLabel.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.ipLabel.setObjectName("ipLabel")

        self.retranslateUi(addDialog)
        QtCore.QMetaObject.connectSlotsByName(addDialog)

    def retranslateUi(self, addDialog):
        _translate = QtCore.QCoreApplication.translate
        addDialog.setWindowTitle(_translate("addDialog", "Adicionar Amigos"))
        self.salvarButton.setText(_translate("addDialog", "Salvar"))
        self.fecharButton.setText(_translate("addDialog", "Fechar"))
        self.nomeLabel.setText(_translate("addDialog", "Nome:"))
        self.ipLabel.setText(_translate("addDialog", "IP:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addDialog = QtWidgets.QDialog()
    ui = Ui_addDialog()
    ui.setupUi(addDialog)
    addDialog.show()
    sys.exit(app.exec_())

