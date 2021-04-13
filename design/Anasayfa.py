from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_anaekran(QtWidgets.QWidget):
    def setupUi(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(451, 341)

        self.lbl_ust = QtWidgets.QLabel(self)
        self.lbl_ust.setGeometry(QtCore.QRect(0, 0, 451, 51))
        self.lbl_ust.setObjectName("lbl_ust")

        self.lbl_alt = QtWidgets.QLabel(self)
        self.lbl_alt.setGeometry(QtCore.QRect(0, 300, 451, 41))
        self.lbl_alt.setObjectName("lbl_alt")

        self.lbl_orta = QtWidgets.QLabel(self)
        self.lbl_orta.setGeometry(QtCore.QRect(0, 50, 451, 251))
        self.lbl_orta.setObjectName("lbl_orta")

        self.lbl_logo = QtWidgets.QLabel(self)
        self.lbl_logo.setGeometry(QtCore.QRect(4, 4, 45, 45))
        self.lbl_logo.setObjectName("lbl_logo")

        self.btn_minimized = QtWidgets.QPushButton(self)
        self.btn_minimized.setGeometry(QtCore.QRect(386, 10, 27, 27))
        self.btn_minimized.setObjectName("btn_minimized")
        self.btn_minimized.setCursor(QtCore.Qt.PointingHandCursor)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setGeometry(QtCore.QRect(420, 10, 27, 27))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_oyunAd = QtWidgets.QLabel(self)
        self.lbl_oyunAd.setGeometry(QtCore.QRect(130, 12, 195, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_oyunAd.setFont(font)
        self.lbl_oyunAd.setObjectName("lbl_oyunAd")

        self.btn_egitim = QtWidgets.QPushButton(self)
        self.btn_egitim.setGeometry(QtCore.QRect(370, 310, 50, 23))
        self.btn_egitim.setObjectName("btn_egitim")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_egitim.setFont(font)
        self.btn_egitim.setCursor(QtCore.Qt.PointingHandCursor)

        self.radioButton_sayi = QtWidgets.QRadioButton(self)
        self.radioButton_sayi.setGeometry(QtCore.QRect(130, 70, 82, 17))
        self.radioButton_sayi.setObjectName("radioButton_sayi")
        self.radioButton_sayi.setChecked(True)
        self.radioButton_sayi.toggled.connect(self.radioKontrol)

        self.radioButton_gorsel = QtWidgets.QRadioButton(self)
        self.radioButton_gorsel.setGeometry(QtCore.QRect(235, 70, 100, 17))
        self.radioButton_gorsel.setObjectName("radioButton_gorsel")


        self.btn_dosyaSec = QtWidgets.QPushButton(self)
        self.btn_dosyaSec.setGeometry(QtCore.QRect(130, 92, 201, 31))
        self.btn_dosyaSec.setObjectName("btn_dosyaSec")
        self.btn_dosyaSec.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_dosyaSec.setEnabled(False)

        self.lbl_boyutAd = QtWidgets.QLabel(self)
        self.lbl_boyutAd.setGeometry(QtCore.QRect(148, 130, 41, 16))
        self.lbl_boyutAd.setObjectName("lbl_boyutAd")

        self.comboBox_boyut = QtWidgets.QComboBox(self)
        self.comboBox_boyut.setGeometry(QtCore.QRect(190, 130, 141, 22))
        self.comboBox_boyut.setObjectName("comboBox_boyut")
        listElemanlari = ["3x3", "4x4", "5x5", "6x6"]
        self.comboBox_boyut.addItems(listElemanlari)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_boyut.setFont(font)

        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(130, 160, 60, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.checkBoxKontrol)

        self.comboBox_sure = QtWidgets.QComboBox(self)
        self.comboBox_sure.setGeometry(QtCore.QRect(190, 160, 141, 22))
        self.comboBox_sure.setObjectName("comboBox_sure")
        listElemanlariSure = ["5 Dakika", "10 Dakika", "15 Dakika", "20 Dakika","25 Dakika","30 Dakika"]
        self.comboBox_sure.addItems(listElemanlariSure)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_sure.setFont(font)
        self.comboBox_sure.setEnabled(False)

        self.btn_basla = QtWidgets.QPushButton(self)
        self.btn_basla.setGeometry(QtCore.QRect(130, 200, 201, 31))
        self.btn_basla.setObjectName("btn_basla")
        self.btn_basla.setCursor(QtCore.Qt.PointingHandCursor)

        self.btn_turnuva = QtWidgets.QPushButton(self)
        self.btn_turnuva.setGeometry(QtCore.QRect(130, 242, 201, 31))
        self.btn_turnuva.setObjectName("btn_turnuva")
        self.btn_turnuva.setCursor(QtCore.Qt.PointingHandCursor)

        self.setStyleSheet(open("Anasayfa.qss","r").read())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_exit.clicked.connect(self.kapat)
        self.btn_minimized.clicked.connect(self.kucult)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.btn_basla.setIcon(QtGui.QIcon("../icons/finishGri.png"))
        self.btn_turnuva.setIcon(QtGui.QIcon("../icons/cupGri.png"))
        self.btn_dosyaSec.setIcon(QtGui.QIcon("../icons/fileGri.png"))
        self.btn_basla.installEventFilter(self)
        self.btn_turnuva.installEventFilter(self)
        self.btn_dosyaSec.installEventFilter(self)

    def eventFilter(self,object,event):
        if object == self.btn_basla:
            if event.type() == QtCore.QEvent.Enter:
                object.setIcon(QtGui.QIcon("../icons/finishBeyaz.png",))
                return True
            elif event.type() == QtCore.QEvent.Leave:
                object.setIcon(QtGui.QIcon("../icons/finishGri.png"))
        elif object == self.btn_turnuva:
            if event.type() == QtCore.QEvent.Enter:
                object.setIcon(QtGui.QIcon("../icons/cupBeyaz.png",))
                return True
            elif event.type() == QtCore.QEvent.Leave:
                object.setIcon(QtGui.QIcon("../icons/cupGri.png"))
        elif object == self.btn_dosyaSec and self.radioButton_gorsel.isChecked():
            if event.type() == QtCore.QEvent.Enter:
                object.setIcon(QtGui.QIcon("../icons/fileBeyaz.png",))
                return True
            elif event.type() == QtCore.QEvent.Leave:
                object.setIcon(QtGui.QIcon("../icons/fileGri.png"))
        return False

    def goster(self):
        self.show()

    def kapat(self):
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Oyun"))
        self.lbl_oyunAd.setText(_translate("self", "Sayı - Görsel Sıralama"))
        self.btn_egitim.setText(_translate("self", "Eğitim"))
        self.radioButton_sayi.setText(_translate("self", "Sayı Modu"))
        self.radioButton_gorsel.setText(_translate("self", "Görsel Modu"))
        self.btn_dosyaSec.setText(_translate("self", "       Dosya Seç"))
        self.lbl_boyutAd.setText(_translate("self", "Boyut :"))
        self.checkBox.setText(_translate("self", "Süre :"))
        self.btn_basla.setText(_translate("self", "          Başla"))
        self.btn_turnuva.setText(_translate("self", "        Turnuva"))

    def kucult(self):
        self.showMinimized()

    def checkBoxKontrol(self):
        if self.checkBox.isChecked():
            self.comboBox_sure.setEnabled(True)
        else:
            self.comboBox_sure.setEnabled(False)

    def radioKontrol(self):
        if self.radioButton_sayi.isChecked():
            self.btn_dosyaSec.setEnabled(False)
        else:
            self.btn_dosyaSec.setEnabled(True)