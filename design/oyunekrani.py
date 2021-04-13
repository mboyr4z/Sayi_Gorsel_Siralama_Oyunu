from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Oyunekrani(QtWidgets.QWidget):
    def setupUi(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(593, 493)

        self.lbl_ust = QtWidgets.QLabel(self)
        self.lbl_ust.setGeometry(QtCore.QRect(0, 0, 651, 50))
        self.lbl_ust.setObjectName("lbl_ust")

        self.lbl_logo = QtWidgets.QLabel(self)
        self.lbl_logo.setGeometry(QtCore.QRect(4, 4, 45, 45))
        self.lbl_logo.setObjectName("lbl_logo")

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setGeometry(QtCore.QRect(560, 10, 27, 27))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setCursor(QtCore.Qt.PointingHandCursor)

        self.btn_minimized = QtWidgets.QPushButton(self)
        self.btn_minimized.setGeometry(QtCore.QRect(525, 10, 27, 27))
        self.btn_minimized.setObjectName("btn_minimized")
        self.btn_minimized.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_oyunAd = QtWidgets.QLabel(self)
        self.lbl_oyunAd.setGeometry(QtCore.QRect(180, 10, 195, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_oyunAd.setFont(font)
        self.lbl_oyunAd.setObjectName("lbl_oyunAd")

        self.lbl_orta = QtWidgets.QLabel(self)
        self.lbl_orta.setGeometry(QtCore.QRect(0, 50, 651, 441))
        self.lbl_orta.setObjectName("lbl_orta")

        self.lbl_sure = QtWidgets.QLabel(self)
        self.lbl_sure.setGeometry(QtCore.QRect(545, 60, 45, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_sure.setFont(font)
        self.lbl_sure.setObjectName("lbl_sure")

        self.btn_sureDurdur = QtWidgets.QPushButton(self)
        self.btn_sureDurdur.setGeometry(QtCore.QRect(535, 90, 30, 30))
        self.btn_sureDurdur.setObjectName("btn_sureDurdur")
        self.btn_sureDurdur.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_sureAd = QtWidgets.QLabel(self)
        self.lbl_sureAd.setGeometry(QtCore.QRect(505, 60, 40, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_sureAd.setFont(font)
        self.lbl_sureAd.setObjectName("lbl_sureAd")

        self.oyunAlan = QtWidgets.QWidget(self)
        self.oyunAlan.setGeometry(QtCore.QRect(50, 60, 450, 380))
        self.oyunAlan.setStyleSheet("background:#006666;")
        self.oyunAlan.setObjectName("oyunAlan")

        self.btngrup = QtWidgets.QButtonGroup(self)
        self.btngrup.setExclusive(True)

        self.btn_home = QtWidgets.QPushButton(self)
        self.btn_home.setGeometry(QtCore.QRect(3, 60, 45,45 ))
        self.btn_home.setObjectName("btn_home")
        self.btn_home.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_alt = QtWidgets.QLabel(self)
        self.lbl_alt.setGeometry(QtCore.QRect(0, 449, 651, 50))
        self.lbl_alt.setObjectName("lbl_alt")

        self.btn_egitim = QtWidgets.QPushButton(self)
        self.btn_egitim.setGeometry(QtCore.QRect(510, 458, 60, 25))
        self.btn_egitim.setObjectName("btn_egitim")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_egitim.setFont(font)
        self.btn_egitim.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_hamleAd = QtWidgets.QLabel(self)
        self.lbl_hamleAd.setGeometry(QtCore.QRect(245, 458, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_hamleAd.setFont(font)
        self.lbl_hamleAd.setObjectName("lbl_hamleAd")

        self.lbl_hamle = QtWidgets.QLabel(self)
        self.lbl_hamle.setGeometry(QtCore.QRect(305, 458, 40, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_hamle.setFont(font)
        self.lbl_hamle.setObjectName("lbl_hamle")
        self.setStyleSheet(open("Anasayfa.qss","r").read())

        self.btn_exit.clicked.connect(self.kapat)
        self.btn_minimized.clicked.connect(self.kucult)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.lbl_oyunAd.setText(_translate("self", "Sayı - Görsel Sıralama"))
        self.lbl_sure.setText(_translate("self", "00:00"))
        self.lbl_sureAd.setText(_translate("self", "Süre :"))
        self.btn_egitim.setText(_translate("self", "Eğitim"))
        self.lbl_hamleAd.setText(_translate("self", "Hamle:"))
        self.lbl_hamle.setText(_translate("self", "0"))

    def goster(self):
        self.show()

    def kapat(self):
        self.close()

    def kucult(self):
        self.showMinimized()