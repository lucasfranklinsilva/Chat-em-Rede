import datetime
import requests
import json
import Ui_Controller
import sys

sys.path.insert(0, '../')
import Global

class Message(object):

    model = None

    def __init__(self, model):
        self.model = model

    def sendMessage(self, view, mutex):
        mutex.acquire()
        objUi = Ui_Controller.Ui(self.model)
        headers = {'content-type': 'application/json'}
        port =  '8000'
        rowId = view.amigosWidget.currentRow()
        receiverData = self.model.select('amigos', 'rowId=%i' % rowId, None, 'id','ip')
        sender = self.model.select('amigos', 'owner=1', None, 'id', 'nome', 'ip')
        message = view.textoEdit.toPlainText()
        self.saveMessage((Global.dict2var(sender,'id')), (Global.dict2var(receiverData,'id')), message)
        objUi.updateChatWindow(view, rowId)

        url = 'http://' + Global.dict2var(receiverData, 'ip') + ":" + port
        data = {'message': message,
                'ip': Global.dict2var(sender, 'ip'),
                'signal': 0}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        mutex.release()

    def saveMessage(self, senderId, receiverId, message):
        self.model.insert('mensagens', mensagem=message, data=datetime.datetime.now(), id_remetente=senderId, id_destinatario=receiverId, flag=0)

    def typing_signal(self, view):

        rowId = view.amigosWidget.currentRow()
        receiverData = self.model.select('amigos', 'rowId=%i' % rowId, None, 'id', 'ip')
        sender = self.model.select('amigos', 'owner=1', None, 'id', 'nome', 'ip')

        print('typing')
        print(Global.dict2var(receiverData, 'ip'))
        print(Global.dict2var(sender, 'ip'))

        headers = {'content-type': 'application/json'}
        port = '8000'

        url = 'http://' + Global.dict2var(receiverData, 'ip') + ":" + port
        data = {'message': '',
                'ip': Global.dict2var(sender, 'ip'),
                'signal': 1}
        response = requests.post(url, data=json.dumps(data), headers=headers)