# -*- coding: utf-8 -*-

"""
PAi 35
Cemodule vérifie la connexion avec le banc pieton
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Consigne(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 344)
        MainWindow.setFixedSize(290, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pos_0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pos_0.setGeometry(QtCore.QRect(10, 60, 62, 22))
        self.pos_0.setMaximum(0)
        self.pos_0.setMinimum(-20)
        self.pos_0.setObjectName("pos_0")

        self.angl = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.angl.setGeometry(QtCore.QRect(170, 60, 62, 22))
        self.angl.setMinimum(-90)
        self.angl.setMaximum(90)
        self.angl.setObjectName("angl")

        self.label_pos_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_pos_0.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.label_pos_0.setObjectName("label_pos_0")

        self.label_angl = QtWidgets.QLabel(self.centralwidget)
        self.label_angl.setGeometry(QtCore.QRect(170, 40, 81, 20))
        self.label_angl.setObjectName("label_angl")

        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(0, 20, 291, 21))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")

        self.Titre1 = QtWidgets.QLabel(self.centralwidget)
        self.Titre1.setGeometry(QtCore.QRect(10, 10, 201, 20))
        self.Titre1.setObjectName("Titre1")

        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(0, 90, 291, 16))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")

        self.Titre2 = QtWidgets.QLabel(self.centralwidget)
        self.Titre2.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.Titre2.setObjectName("Titre2")

        self.label_pos_d = QtWidgets.QLabel(self.centralwidget)
        self.label_pos_d.setGeometry(QtCore.QRect(10, 120, 101, 21))
        self.label_pos_d.setObjectName("label_pos_d")

        self.pos_d = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pos_d.setGeometry(QtCore.QRect(10, 140, 62, 22))
        self.pos_d.setMaximum(20)
        self.pos_d.setMinimum(-20)
        self.pos_d.setObjectName("pos_d")

        self.pos_ar = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pos_ar.setGeometry(QtCore.QRect(170, 140, 62, 22))
        self.pos_ar.setMaximum(20)
        self.pos_ar.setMinimum(self.pos_d.value())
        self.pos_ar.setObjectName("pos_ar")

        self.label_pos_ar = QtWidgets.QLabel(self.centralwidget)
        self.label_pos_ar.setGeometry(QtCore.QRect(170, 120, 81, 20))
        self.label_pos_ar.setObjectName("label_pos_ar")

        self.Titre3 = QtWidgets.QLabel(self.centralwidget)
        self.Titre3.setGeometry(QtCore.QRect(10, 180, 61, 16))
        self.Titre3.setObjectName("Titre3")

        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(0, 170, 291, 16))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")

        self.T_acc = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.T_acc.setGeometry(QtCore.QRect(10, 220, 62, 22))
        self.T_acc.setMaximum(3)
        self.T_acc.setObjectName("T_acc")

        self.label_T_acc = QtWidgets.QLabel(self.centralwidget)
        self.label_T_acc.setGeometry(QtCore.QRect(10, 200, 121, 21))
        self.label_T_acc.setObjectName("label_T_acc")

        self.T_dec = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.T_dec.setGeometry(QtCore.QRect(10, 260, 62, 22))
        self.T_acc.setMaximum(3)
        self.T_dec.setObjectName("T_dec")

        self.label_T_dec = QtWidgets.QLabel(self.centralwidget)
        self.label_T_dec.setGeometry(QtCore.QRect(10, 240, 101, 21))
        self.label_T_dec.setObjectName("label_T_dec")

        self.V = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.V.setGeometry(QtCore.QRect(10, 300, 62, 22))
        self.V.setMaximum(25)
        self.V.setObjectName("V")

        self.label_V = QtWidgets.QLabel(self.centralwidget)
        self.label_V.setGeometry(QtCore.QRect(10, 280, 101, 21))
        self.label_V.setObjectName("label_V")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_pos_0.setText(_translate("MainWindow", "Position par rapport au 0"))
        self.label_angl.setText(_translate("MainWindow", "Angle (en °)"))
        self.Titre1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">La "
                                                     "consigne</span></p></body></html>"))
        self.Titre2.setText(_translate("MainWindow", "<b>Le trajet</b>"))
        self.label_pos_d.setText(_translate("MainWindow", "Position de départ"))
        self.label_pos_ar.setText(_translate("MainWindow", "Position d\'arrêt"))
        self.Titre3.setText(_translate("MainWindow", "<b>Le trajet</b>"))
        self.label_T_acc.setText(_translate("MainWindow", "Temps d\'accéleration"))
        self.label_T_dec.setText(_translate("MainWindow", "Temps décélération"))
        self.label_V.setText(_translate("MainWindow", "Vitesse"))
        self.pushButton.setText(_translate("MainWindow", "Valider"))



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Consigne()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()