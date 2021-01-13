from gui1 import Consigne
from gui0 import Connection
from PyQt5 import QtWidgets,QtCore
import sys
import TCP_Client
import time

TIMEOUT=5
DEBUG = False
PORT1 = 50007
PORT2 = 50008
class Wait(QtCore.QThread):
    def run(self):
        if DEBUG:
            time.sleep(TIMEOUT)
        else:
            while TCP_Client.handshake():
                pass

class Main(object):
    def __init__(self):
        self.Window1 = QtWidgets.QMainWindow()
        self.conn = Connection()
        self.conn.setupUi(self.Window1)
        self.Window2 = QtWidgets.QMainWindow()
        self.cons = Consigne()
        self.cons.setupUi(self.Window2)
        self.Window1.show()
        self.wait = Wait()
        self.status=''
        self.wait.finished.connect(self.togglewin)
        self.wait.start()
        self.cons.pushButton.clicked.connect(self.sendData)


    def togglewin(self):
        self.Window1.hide()
        self.Window2.show()

    def sendData(self):
        data = [self.cons.pos_0.value(), self.cons.angl.value(), self.cons.pos_d.value(), self.cons.pos_ar.value(),
                self.cons.T_acc.value(), self.cons.T_dec.value(), self.cons.V.value()]
        if DEBUG:
            print(data)
        else:
            print(data)
            self.status=TCP_Client.send_data(data,PORT2)

if __name__=='__main__':
    app=app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

