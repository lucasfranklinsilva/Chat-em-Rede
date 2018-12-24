from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys
import Message_Controller
import User_Controller
import Ui_Controller


sys.path.insert(0, '../')
import Global

#class factory
def MakeHandlerClass(objView, objController):
    class Server(BaseHTTPRequestHandler):

        def __init__(self, *args, **kwargs):
            super(Server, self).__init__(*args, **kwargs)

        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_HEAD(self):
            self._set_headers()

        def do_POST(self):

            content_length = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            data = json.loads(post_body.decode('utf-8'))

            mensagem = data['message']
            ip = data['ip']
            signal = data['signal']

            self.wfile.write(mensagem.encode('utf-8'))

            friendId = objController.checkIP(ip)
            friendRowId = objController.rowId(friendId)
            friendName = objController.nameById(friendId)

            if signal == 0:
                if friendId is not 0:
                    objController.saveMessage(friendId, objController.MyID(), mensagem)
                    objController.updateChatWindow(objView, friendRowId)
                    objView.messagensListWidget.scrollToBottom()
            elif signal == 1:
                objView.textoLabel.setText('%s está digitando...'%friendName)
                signal = -1
            elif signal == -1:
                objView.textoLabel.setText('Texto')

            print(mensagem)
            print(ip)
            print(signal)
    return Server

def run(objView, mainController):
    server_address = ('', 8000)
    Server = MakeHandlerClass(objView, mainController)
    httpd = HTTPServer(server_address, Server)
    print
    'Starting httpd...'
    httpd.serve_forever()
