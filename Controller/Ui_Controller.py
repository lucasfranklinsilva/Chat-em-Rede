from PyQt5 import QtWidgets, QtGui
import sys
import User_Controller
import datetime

sys.path.insert(0, '../')
import Global
class Ui(object):

    model = None

    def __init__(self, model):
        self.model = model

    def updateListaAmigos(self, view):
        ansArray = self.model.select('amigos', 'owner != 1', 'nome', 'nome', 'id')
        view.amigosWidget.clear()
        for row in ansArray:
            item = QtWidgets.QListWidgetItem(str(row['nome']))
            view.amigosWidget.addItem(item)
            self.updateListId(view.amigosWidget.row(item),row['id'])

    def updateListId(self, listId, userId):
        self.model.update('amigos', 'id = %i'%userId, rowId=listId)

    def updateChatWindow(self, view, rowId):

        if rowId == view.amigosWidget.row(view.amigosWidget.currentItem()):
            objUser = User_Controller.User(self.model)
            view.messagensListWidget.clear()
            ansArray = self.model.select('amigos', 'rowId = %i' % rowId, None, 'id', 'nome')
            freindId = Global.dict2var(ansArray, 'id')
            name = Global.dict2var(ansArray, 'nome')
            view.mengagemLabel.setText('Conversa com %s' % name)
            messages = self.model.select('mensagens', '(id_remetente = %i AND id_destinatario = %i) OR (id_remetente = %i AND id_destinatario = %i)'%(objUser.MyID(), freindId, freindId, objUser.MyID()), 'data')

            if messages:
                for row in messages:
                    item = QtWidgets.QListWidgetItem(str(objUser.nameById(row['id_remetente'])) + ' disse:  ' + str(row['data'].strftime("%d/%m/%Y - %H:%M")))
                    item.setFont(QtGui.QFont('Verdana', 8, QtGui.QFont.Bold))
                    view.messagensListWidget.addItem(item)
                    message = QtWidgets.QListWidgetItem(str(row['mensagem']))
                    view.messagensListWidget.addItem(message)
                    view.messagensListWidget.scrollToBottom()
                    view.messagensListWidget.scrollToItem(message, 0)
        else:
            item = view.amigosWidget.item(rowId)
            item.setFont(QtGui.QFont('Verdana', 7, QtGui.QFont.Bold))
