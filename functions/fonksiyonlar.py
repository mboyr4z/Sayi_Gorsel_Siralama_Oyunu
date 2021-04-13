from PyQt5.QtCore import *
import tkinter as tk
from tkinter import filedialog


class function (object):

    def sayfaGecisi(self,ana,oyun,bild,egitim,degisken,alg):
        self.ana=ana
        self.oyun=oyun
        self.bild=bild
        self.egitim=egitim
        self.degisken=degisken
        self.alg=alg

        ana.btn_basla.clicked.connect(self.normal_Basla)
        ana.btn_turnuva.clicked.connect(self.turnuva_Basla)
        oyun.btn_home.clicked.connect(self.anaEkranCagir)
        oyun.btn_egitim.clicked.connect(self.egitimEkranCagir)
        ana.btn_egitim.clicked.connect(self.egitimEkranCagir)
        oyun.btngrup.buttonClicked[int].connect(alg.butonTikla)
        bild.btn_next.clicked.connect(self.levelAtla)

        ana.comboBox_sure.currentTextChanged.connect(self.sureDegis)
        ana.comboBox_boyut.currentTextChanged.connect(self.boyutDegis)
        self.timer = QTimer(oyun)
        self.timer.timeout.connect(self.showTime)

        oyun.btn_sureDurdur.clicked.connect(self.pause_action)
        self.bild.btn_anasayfa.clicked.connect(self.anaEkranCagir)
        self.bild.btn_restart.clicked.connect(self.restart)

        self.dakika=0
        self.saniye=0
        self.count=5*60*10
        self.timer.start(100)
        self.start = False

        self.ana.btn_dosyaSec.clicked.connect(self.dosyaKonum)

    def levelAtla(self):
        self.bild.close()
        self.degisken.turnuvaSeviye += 1
        self.alg.temizle()
        self.oyun.btn_sureDurdur.setEnabled(True)
        self.alg.butonOlustur()
        self.pause_action()


    def normal_Basla(self):
        self.sureDegis()
        if self.ana.radioButton_gorsel.isChecked() == True and self.degisken.konum == "":
            self.bild.lbl_gorsel.setStyleSheet("background:url('../icons/warn.png'); background-repeat:no-repeat;")
            self.bild.lbl_mesaj.setText("Görsel Seçilmedi! Lütfen Görsel Seçiniz...")
            self.bild.btn_next.setVisible(False)
            self.bild.btn_anasayfa.setVisible(False)
            self.bild.btn_restart.setVisible(False)
            self.bild.show()
        else:
            self.degisken.mod = "normal"
            self.oyunEkranCagir()
            self.sureIslemi()
            self.alg.butonOlustur()


    def turnuva_Basla(self):
        if self.ana.radioButton_gorsel.isChecked() == True and self.degisken.dosyaKonum == "":
            self.bild.lbl_gorsel.setStyleSheet("background:url('../icons/warn.png'); background-repeat:no-repeat;")
            self.bild.lbl_mesaj.setText("Görsel Seçilmedi! Lütfen Görsel Seçiniz...")
            self.bild.btn_next.setVisible(False)
            self.bild.btn_anasayfa.setVisible(False)
            self.bild.btn_restart.setVisible(False)
            self.bild.show()
        else:
            self.degisken.mod = "turnuva"
            self.oyunEkranCagir()
            self.sureIslemi()
            self.alg.butonOlustur()



    def dosyaKonum(self):
        root = tk.Tk()
        root.withdraw()
        self.degisken.konum = filedialog.askopenfilename()


    def oyunEkranCagir(self):
        self.oyun.btn_sureDurdur.setStyleSheet("background:none; background:url('../icons/pause.png');")
        self.oyun.goster()
        self.oyun.btn_sureDurdur.setEnabled(True)
        self.ana.kapat()

    def sureIslemi(self):
        self.degisken.sureKontrol = 1
        self.start = True
        if self.ana.checkBox.isChecked() == False:
            self.oyun.lbl_sure.setText("00:00")
            self.timer.stop()
        else:
            self.timer.start(100)
            self.sureDegis()

    def anaEkranCagir(self):
        self.oyun.kapat()
        self.ana.goster()
        self.sureDegis()
        self.alg.temizle()
        self.oyun.btn_sureDurdur.setEnabled(True)
        self.bild.close()
        self.degisken.turnuvaSeviye = 0
        self.boyutDegis()
        self.bild.btn_next.setEnabled(True)

    def egitimEkranCagir(self):
        self.egitim.goster()

    def showTime(self):
        if self.start:
            self.count -= 1
            if self.count == 0:
                self.start = False
                self.oyun.lbl_sure.setText("00:00")
                self.bild.lbl_gorsel.setStyleSheet("background:url('../icons/warning.png'); background-repeat:no-repeat;")
                self.bild.lbl_mesaj.setText("Süre Doldu! Tekrar Deneyebilirsiniz...")
                self.bild.show()
                self.pause_action()
                self.bild.btn_next.setEnabled(False)
                self.oyun.btn_sureDurdur.setEnabled(False)
                self.alg.butonPasif()
        if self.start:
            self.saniye = str(int(int(self.count) / 10)%60)
            self.dakika=str(int(int(self.count)/10/60))

            self.oyun.lbl_sure.setText(self.dakika+":"+self.saniye)

    def start_action(self):
        self.start = True

        if self.count == 0:
            self.start = False

    def pause_action(self):
        if self.degisken.sureKontrol==1:
            self.oyun.btn_sureDurdur.setStyleSheet("background:none; background:url('../icons/play.png');")
            self.degisken.sureKontrol=0
            self.start = False
            self.alg.butonPasif()
        else:
            self.oyun.btn_sureDurdur.setStyleSheet("background:none; background:url('../icons/pause.png');")
            self.degisken.sureKontrol = 1
            self.start = True
            self.alg.butonAktif()


    def sureDegis(self):
        if self.ana.comboBox_sure.currentText() == "5 Dakika":
            self.degisken.sure = 5
        elif self.ana.comboBox_sure.currentText() == "10 Dakika":
            self.degisken.sure = 10
        elif self.ana.comboBox_sure.currentText() == "15 Dakika":
            self.degisken.sure = 15
        elif self.ana.comboBox_sure.currentText() == "20 Dakika":
            self.degisken.sure = 20
        elif self.ana.comboBox_sure.currentText() == "25 Dakika":
            self.degisken.sure = 25
        else:
            self.degisken.sure = 30

        self.count =self.degisken.sure*60*10

    def boyutDegis(self):
        if self.ana.comboBox_boyut.currentText() =="3x3":
            self.degisken.boyut=3
        elif self.ana.comboBox_boyut.currentText() =="4x4":
            self.degisken.boyut=4
        elif self.ana.comboBox_boyut.currentText() =="5x5":
            self.degisken.boyut=5
        else:
            self.degisken.boyut=6

    def restart(self):
        self.alg.temizle()
        self.sureDegis()
        self.start_action()
        self.pause_action()
        self.alg.butonOlustur()
        self.oyun.btn_sureDurdur.setEnabled(True)
        self.bild.close()
        self.bild.btn_next.setEnabled(True)