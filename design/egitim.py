from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Egitim(QtWidgets.QWidget):
    def setupUi(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(800, 800)
        self.setStyleSheet(open("Anasayfa.qss","r").read())

        self.lbl_ust = QtWidgets.QLabel(self)
        self.lbl_ust.setGeometry(QtCore.QRect(0, 0, 800, 51))
        self.lbl_ust.setStyleSheet("")
        self.lbl_ust.setText("")
        self.lbl_ust.setObjectName("lbl_ust")

        self.lbl_logo = QtWidgets.QLabel(self)
        self.lbl_logo.setGeometry(QtCore.QRect(4, 4, 45, 45))
        self.lbl_logo.setStyleSheet("")
        self.lbl_logo.setText("")
        self.lbl_logo.setObjectName("lbl_logo")

        self.lbl_oyunAd = QtWidgets.QLabel(self)
        self.lbl_oyunAd.setGeometry(QtCore.QRect(300, 13, 195, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_oyunAd.setFont(font)
        self.lbl_oyunAd.setObjectName("lbl_oyunAd")

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setGeometry(QtCore.QRect(765, 15, 27, 27))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setCursor(QtCore.Qt.PointingHandCursor)

        self.btn_minimized = QtWidgets.QPushButton(self)
        self.btn_minimized.setGeometry(QtCore.QRect(730, 15, 27, 27))
        self.btn_minimized.setObjectName("btn_minimized")
        self.btn_minimized.setCursor(QtCore.Qt.PointingHandCursor)

        self.lbl_orta = QtWidgets.QLabel(self)
        self.lbl_orta.setGeometry(QtCore.QRect(0, 51, 800, 698))
        self.lbl_orta.setObjectName("lbl_orta")

        self.lbl_alt = QtWidgets.QLabel(self)
        self.lbl_alt.setGeometry(QtCore.QRect(0, 749, 800, 51))
        self.lbl_alt.setText("")
        self.lbl_alt.setObjectName("lbl_alt")

        self.lbl_aciklama = QtWidgets.QLabel(self)
        self.lbl_aciklama.setGeometry(QtCore.QRect(15, 60, 760, 650))
        self.lbl_aciklama.setObjectName("lbl_aciklama")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_aciklama.setFont(font)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_exit.clicked.connect(self.kapat)
        self.btn_minimized.clicked.connect(self.kucult)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.lbl_oyunAd.setText(_translate("self", "Say?? - G??rsel S??ralama"))
        self.lbl_aciklama.setText(_translate("self", "                                                            OYUNA BA??LARKEN    \n\n"
        "\n->>   Oyuna ba??larken oynamak istedi??iniz modu (Say?? modu - G??rsel modu) se??ebilirsiniz.\n"
        "\n->>   G??rsel modu se??tiyseniz 'Dosya Se??' butonunu kullanarak g??rsel se??ebilirsiniz.\n"
        "\n->>   Oyunda olmas??n?? istedi??iniz kare say??s??n?? 'Boyut' k??s??m??ndan se??ebilirsiniz.\n"
        "\n->>   Oyunda olmas??n?? istedi??iniz s??re miktar??n?? 'S??re' k??s??m??ndan se??ebilirsiniz.\n"
        "\n->>   'Ba??la' butonu ile se??ti??iniz ??zelliklere uygun olarak oyuna ba??layabilirsiniz.\n"
        "\n->>   'Turnuva' butonu ile en k??????k boyutta oyuna ba??layarak en b??y??k boyuta kadar ilerleyebilirsiniz.\n\n"
        "                                                                     OYNANI??    \n\n"
        "\n->>   Kar??????k gelen say??lar?? 1'den ba??layarak ard??????k ??ekilde s??ralaman??z istenmektedir.\n"
        "\n->>   Kar??????k gelen g??rsel par??alar??n?? g??rsel tamamlanana kadar s??ralaman??z istenmektedir.\n"
        "\n->>   Her par??a i??in ??zerine 1 kez t??klaman??z yeterli olacakt??r ve hareket edemeyen par??alar oldu??u\n         gibi kalmaktad??r.\n"
        "\n->>   Her bir par??an??n hareketi +1 hamle say??s?? olarak alt k??s??mda g??r??nt??lenir.Buna hareket\n          edemeyen par??alar dahil de??ildir.\n"
        "\n->>   Oyunu s??reli ba??latm???? iseniz s??re doldu??u zaman oyun bitmektedir.??sterseniz bildirim\n          ekran??ndayken oyunu tekrar ba??latabilir veya ana men??ye d??nebilirsiniz."))

    def goster(self):
        self.show()

    def kapat(self):
        self.close()

    def kucult(self):
        self.showMinimized()

