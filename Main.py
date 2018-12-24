import sys

sys.path.insert(0, './Model')
import Model

sys.path.insert(0, './Controller')
import Message_Controller
import Server_Controller
import Ui_Controller
import User_Controller

sys.path.insert(0, './View')
import View

class model(Model.My_DB):
    def __init__(self):
        super(self.__class__, self).__init__('127.0.0.1', 'lufs', '1234', 'chat')

class controller(Message_Controller.Message, Ui_Controller.Ui, User_Controller.User):
    def __init__(self, model):
        super(self.__class__, self).__init__(model)

class view(View.View):
    def __init__(self, controller):
        super(self.__class__, self).__init__(controller)

def MainWindow():

    modelObj = model()
    controllerObj = controller(modelObj)
    app = QtWidgets.QApplication(sys.argv)
    form = view(controllerObj)

    Thread2 = threading.Thread(target=Server_Controller.run, args=(form,controllerObj))
    Thread2.start()

    form.show()
    sys.exit(app.exec_())

def main():
    Thread1 = threading.Thread(target = MainWindow)
    Thread1.start()


if __name__ == '__main__':
    main()

