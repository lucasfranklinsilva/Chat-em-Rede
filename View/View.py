from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import threading

import add
import chat

class View(QtWidgets.QMainWindow, chat.Ui_MainWindow):

    controllerObj = None

    def __init__(self, controller, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.controllerObj = controller
        controller.updateListaAmigos(self)

        #Botões
        self.addButton.clicked.connect(self.openDialog)
        self.amigosWidget.itemClicked.connect(self.item_click)
        self.enviarButton.clicked.connect(self.messageProcess)
        self.textoEdit.textChanged.connect(self.typing_signal)

    def typing_signal(self):
        self.controllerObj.typing_signal(self)

    def messageProcess(self):
        mutex = threading.Lock()
        Thread3 = threading.Thread(target=self.controllerObj.sendMessage, args=(self,mutex))
        Thread3.start()
        mutex.acquire()
        self.textoEdit.clear()
        mutex.release()

    def item_click(self, item):
        self.controllerObj.updateChatWindow(self, int(self.amigosWidget.row(item)))

    def openDialog(self):
        d = Dialog(self.controllerObj, self)
        d.exec_()
        self.controllerObj.updateListaAmigos(self)


class Dialog(QtWidgets.QDialog, add.Ui_addDialog):

    controller = None
    parentWindow = None

    def __init__(self, controllerObj, Window, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.controller = controllerObj
        self.parentWindow = Window
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regulare expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)

        self.ipEdit.setValidator(ipValidator)
        self.salvarButton.clicked.connect(self.add_amigo)
        self.fecharButton.clicked.connect(self.close)

    def add_amigo(self):

        Thread4 = threading.Thread(target=self.controller.add_amigo, args=(self,))
        Thread4.start()

