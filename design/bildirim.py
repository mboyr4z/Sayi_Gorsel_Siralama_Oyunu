from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_bildirim(QtWidgets.QWidget):
    def setupUi(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(451, 202)
        self.lbl_ust = QtWidgets.QLabel(self)
        self.lbl_ust.setGeometry(QtCore.QRect(0, 0, 451, 51))
        self.lbl_ust.setStyleSheet("")
        self.lbl_ust.setText("")
        self.lbl_ust.setObjectName("lbl_ust")

        self.lbl_logo = QtWidgets.QLabel(self)
        self.lbl_logo.setGeometry(QtCore.QRect(4, 4, 45, 45))
        self.lbl_logo.setStyleSheet("")
        self.lbl_logo.setText("")
        self.lbl_logo.setObjectName("lbl_logo")

        self.lbl_oyunAd = QtWidgets.QLabel(self)
        self.lbl_oyunAd.setGeometry(QtCore.QRect(125, 15, 195, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_oyunAd.setFont(font)
        self.lbl_oyunAd.setObjectName("lbl_oyunAd")

        self.btn_minimized = QtWidgets.QPushButton(self)
        self.btn_minimized.setGeometry(QtCore.QRect(380, 10, 27, 27))
        self.btn_minimized.setObjectName("btn_minimized")
        self.btn_minimized.setCursor(QtCore.Qt.PointingHandCursor)


        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setGeometry(QtCore.QRect(415, 10, 27, 27))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_orta = QtWidgets.QLabel(self)
        self.lbl_orta.setGeometry(QtCore.QRect(0, 51, 451, 151))
        self.lbl_orta.setStyleSheet("border:3px solid; border-color:#006666;")
        self.lbl_orta.setText("")
        self.lbl_orta.setObjectName("lbl_orta")

        self.btn_anasayfa = QtWidgets.QPushButton(self)
        self.btn_anasayfa .setGeometry(QtCore.QRect(10, 140, 131, 31))
        self.btn_anasayfa .setObjectName("btn_anasayfa")
        self.btn_anasayfa.setCursor(QtCore.Qt.PointingHandCursor)

        self.btn_restart = QtWidgets.QPushButton(self)
        self.btn_restart.setGeometry(QtCore.QRect(150, 140, 131, 31))
        self.btn_restart.setObjectName("btn_restart")
        self.btn_restart.setCursor(QtCore.Qt.PointingHandCursor)

        self.btn_next = QtWidgets.QPushButton(self)
        self.btn_next.setGeometry(QtCore.QRect(290, 140, 141, 31))
        self.btn_next.setObjectName("btn_next")
        self.btn_next.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_gorsel = QtWidgets.QLabel(self)
        self.lbl_gorsel.setGeometry(QtCore.QRect(30, 70, 55, 55))
        self.lbl_gorsel.setObjectName("lbl_gorsel")

        self.lbl_mesaj = QtWidgets.QLabel(self)
        self.lbl_mesaj.setGeometry(QtCore.QRect(130, 75, 290, 40))
        self.lbl_mesaj.setObjectName("lbl_mesaj")
        self.lbl_mesaj.setStyleSheet("color:black;font-size:16px;")

        self.setStyleSheet(open("Anasayfa.qss","r").read())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_exit.clicked.connect(self.kapat)
        self.btn_minimized.clicked.connect(self.kucult)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.btn_anasayfa.installEventFilter(self)
        self.btn_anasayfa.setIcon(QtGui.QIcon("../icons/anasayfaGri.png"))
        self.btn_restart.installEventFilter(self)
        self.btn_restart.setIcon(QtGui.QIcon("../icons/repeatGri.png"))
        self.btn_next.installEventFilter(self)
        self.btn_next.setIcon(QtGui.QIcon("../icons/nextGri.png"))

    def eventFilter(self,object,event):
        if object == self.btn_anasayfa:
            if event.type() == QtCore.QEvent.Enter:
                object.setIcon(QtGui.QIcon("../icons/anasayfaBeyaz.png",))
                return True
            elif event.type() == QtCore.QEvent.Leave:
                object.setIcon(QtGui.QIcon("../icons/anasayfaGri.png"))
        elif object == self.btn_restart:
            if event.type() == QtCore.QEvent.Enter:
                object.setIcon(QtGui.QIcon("../icons/repeatBeyaz.png",))
                return True
            elif event.type() == QtCore.QEvent.Leave:
                object.setIcon(QtGui.QIcon("../icons/repeatGri.png"))
        elif object == self.btn_next:
            if event.type()==QtCore.QEvent.Enter and object.isEnabled()==False:
                object.setIcon(QtGui.QIcon("../icons/nextGri.png"))
            elif event.type() == QtCore.QEvent.Enter:
                object.setIcon(QtGui.QIcon("../icons/nextBeyaz.png",))
                return True
            elif event.type() == QtCore.QEvent.Leave:
                object.setIcon(QtGui.QIcon("../icons/nextGri.png"))
        return False

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.lbl_oyunAd.setText(_translate("self", "Sayı - Görsel Sıralama"))
        self.btn_anasayfa .setText(_translate("self", "    Anasayfa"))
        self.btn_restart.setText(_translate("self", "  Tekrar Oyna"))
        self.btn_next.setText(_translate("self", "  Sonraki Aşama"))
        self.lbl_mesaj.setText(_translate("self", "Mesaj"))

    def goster(self):
        self.show()

    def kapat(self):
        self.close()
        self.btn_next.setEnabled(True)

    def kucult(self):
        self.showMinimized()