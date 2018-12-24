from PyQt5 import QtWidgets, QtGui
import sys
sys.path.insert(0, '../')
import Global

class User(object):

    model = None

    def __init__(self, model):
        self.model = model

    def MyID(self):
        return Global.dict2var(self.model.select('amigos', 'owner = 1', None, 'id'), 'id')

    def rowId(self, userId):
        return Global.dict2var(self.model.select('amigos', 'id = %i'%userId, None, 'rowId'), 'rowId')


    def nameById(self, userId):
        return Global.dict2var(self.model.select('amigos', 'id = %i'%userId, None, 'nome'), 'nome')

    def checkIP(self, IP):
        result = self.model.select('amigos', 'ip = "%s"' % IP, None, 'id')
        if result:
            return Global.dict2var(result, 'id')
        else:
            return 0

    def add_amigo(self, view):
        if self.checkIP(str(view.ipEdit.text())) > 0:
            #QtWidgets.QMessageBox.about(view, "Error", "IP Já Cadastrado!")
            return False
        else:
            self.model.insert('amigos', nome=str(view.nomeEdit.text()), ip=str(view.ipEdit.text()), rowId='0', owner='0')
            view.close()
            return True

