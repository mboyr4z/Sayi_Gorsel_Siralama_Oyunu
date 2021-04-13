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
        self.lbl_oyunAd.setText(_translate("self", "Sayı - Görsel Sıralama"))
        self.lbl_aciklama.setText(_translate("self", "                                                            OYUNA BAŞLARKEN    \n\n"
        "\n->>   Oyuna başlarken oynamak istediğiniz modu (Sayı modu - Görsel modu) seçebilirsiniz.\n"
        "\n->>   Görsel modu seçtiyseniz 'Dosya Seç' butonunu kullanarak görsel seçebilirsiniz.\n"
        "\n->>   Oyunda olmasını istediğiniz kare sayısını 'Boyut' kısımından seçebilirsiniz.\n"
        "\n->>   Oyunda olmasını istediğiniz süre miktarını 'Süre' kısımından seçebilirsiniz.\n"
        "\n->>   'Başla' butonu ile seçtiğiniz özelliklere uygun olarak oyuna başlayabilirsiniz.\n"
        "\n->>   'Turnuva' butonu ile en küçük boyutta oyuna başlayarak en büyük boyuta kadar ilerleyebilirsiniz.\n\n"
        "                                                                     OYNANIŞ    \n\n"
        "\n->>   Karışık gelen sayıları 1'den başlayarak ardışık şekilde sıralamanız istenmektedir.\n"
        "\n->>   Karışık gelen görsel parçalarını görsel tamamlanana kadar sıralamanız istenmektedir.\n"
        "\n->>   Her parça için üzerine 1 kez tıklamanız yeterli olacaktır ve hareket edemeyen parçalar olduğu\n         gibi kalmaktadır.\n"
        "\n->>   Her bir parçanın hareketi +1 hamle sayısı olarak alt kısımda görüntülenir.Buna hareket\n          edemeyen parçalar dahil değildir.\n"
        "\n->>   Oyunu süreli başlatmış iseniz süre dolduğu zaman oyun bitmektedir.İsterseniz bildirim\n          ekranındayken oyunu tekrar başlatabilir veya ana menüye dönebilirsiniz."))

    def goster(self):
        self.show()

    def kapat(self):
        self.close()

    def kucult(self):
        self.showMinimized()

