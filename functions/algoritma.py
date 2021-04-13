import random
from PyQt5 import QtCore, QtGui, QtWidgets
from SayiSiralama.functions import resimParcalama
import os

class algoritma (object):

    bosKonumX = 0
    bosKonumY = 0
    def constructure(self,ana,oyun,bild,egitim,degisken,fonk):
        self.ana=ana
        self.oyun=oyun
        self.bild=bild
        self.egitim=egitim
        self.degisken=degisken
        self.fonk = fonk


    def butonOlustur(self):

        if self.degisken.mod == "turnuva":
            seviye = self.degisken.turnuvaSeviye
            if seviye == 0:
                self.degisken.boyut = 3
            elif seviye == 1:
                self.degisken.boyut = 4
            elif seviye == 2:
                self.degisken.boyut = 5
            else:
                self.degisken.boyut = 6

        self.genislik = int(450/self.degisken.boyut)
        self.yukseklik = int(380/self.degisken.boyut)
        self.bosKonumX = self.genislik * (self.degisken.boyut - 1)
        self.bosKonumY = self.yukseklik * (self.degisken.boyut - 1)
        solkosex = int(0)
        solkosey = int(0)

        butonid = 0
        sayilar=[]
        karisikSayilar=[]

        for i in range(0,self.degisken.boyut**2-1):
            sayilar.append(i)

        for i in range(0,self.degisken.boyut**2-1):
            rand=random.randint(0,len(sayilar)-1)
            karisikSayilar.append(sayilar[rand])
            sayilar.pop(rand)

        if self.ana.radioButton_sayi.isChecked():
            for i in range(0, self.degisken.boyut):
                for j in range(0, self.degisken.boyut):
                    buton = QtWidgets.QPushButton(self.oyun.oyunAlan)
                    buton.setGeometry(int(solkosex), int(solkosey), int(self.genislik), int(self.yukseklik))
                    buton.setStyleSheet("font-size:18px;color:white;border:1px solid;border-color:white;border-radius:3px;background: #4682B4;")
                    buton.setText(str((karisikSayilar[butonid])+1))
                    buton.show()
                    self.oyun.btngrup.addButton(buton, karisikSayilar[butonid])
                    self.degisken.listButon.append(buton)
                    butonid += 1
                    solkosex += self.genislik
                    if butonid == (self.degisken.boyut**2-1):
                        break
                solkosex = int(0)
                solkosey += self.yukseklik
        else:
            resimParcalama.parcala(self.degisken.konum,self.degisken.boyut)
            for i in range(0, self.degisken.boyut):
                for j in range(0, self.degisken.boyut):
                    buton = QtWidgets.QPushButton(self.oyun.oyunAlan)
                    buton.setGeometry(int(solkosex), int(solkosey), int(self.genislik), int(self.yukseklik))
                    indis=karisikSayilar[butonid]
                    konum="../functions/parcaliResimler/"+str(indis)+".jpg"
                    buton.setStyleSheet("border:none;background:url("+konum+");")
                    buton.show()
                    self.oyun.btngrup.addButton(buton, karisikSayilar[butonid])
                    self.degisken.listButon.append(buton)
                    butonid += 1
                    solkosex += self.genislik
                    if butonid == (self.degisken.boyut**2-1):
                        break
                solkosex = int(0)
                solkosey += self.yukseklik
            self.resimlerisil()

    def resimlerisil(self):
        os.chdir("../functions/parcaliResimler")
        for i in os.listdir("."):
            if i.endswith(".jpg") or i.endswith(".png"):
                os.remove(i)
        os.chdir("../../design")

    def temizle(self):
        for i in self.oyun.btngrup.buttons():
            i.close()
        self.oyun.btngrup=QtWidgets.QButtonGroup(self.oyun)
        self.oyun.btngrup.setExclusive(True)
        self.oyun.btngrup.buttonClicked[int].connect(self.butonTikla)
        self.degisken.hamleSayisi=0
        self.oyun.lbl_hamle.setText(str(0))
        self.degisken.listButon.clear()



    def butonTikla(self,id):
        for i in self.oyun.btngrup.buttons():
            if i is self.oyun.btngrup.button(id):
                if(self.satirSutunKontrol(i)):
                    yon = self.hangiYon(i)

                    self.degisken.hamleSayisi += 1
                    self.oyun.lbl_hamle.setText(str(self.degisken.hamleSayisi))

                    if yon == "asagi":
                        self.asagiGit(i.x(),i.y())
                    elif yon == "yukari":
                        self.yukariGit(i.x(),i.y())
                    elif yon == "sag":
                        self.sagaGit(i.x(),i.y())
                    else:
                        self.solaGit(i.x(),i.y())

                    if (self.bittimi()):
                        if self.degisken.mod == "turnuva":
                            if self.degisken.turnuvaSeviye == 3:
                                self.bild.lbl_gorsel.setStyleSheet("background:url('../icons/hand.png'); background-repeat:no-repeat;")
                                self.bild.lbl_mesaj.setText("Tebrikler! Turnuvayı Bitirdiniz :)")
                                self.bild.show()
                                self.fonk.pause_action()
                                self.bild.btn_next.setEnabled(False)
                                self.oyun.btn_sureDurdur.setEnabled(False)
                                self.butonPasif()

                            else:
                                self.bild.lbl_gorsel.setStyleSheet(
                                    "background:url('../icons/hand.png'); background-repeat:no-repeat;")
                                self.bild.lbl_mesaj.setText("Tebrikler! Turnuvanın "+ str(self.degisken.turnuvaSeviye + 1)+". Seviyesini Bitirdiniz :)")
                                self.bild.show()
                                self.fonk.pause_action()
                                self.oyun.btn_sureDurdur.setEnabled(False)
                                self.butonPasif()
                        else:
                            self.bild.lbl_gorsel.setStyleSheet("background:url('../icons/hand.png'); background-repeat:no-repeat;")
                            self.bild.lbl_mesaj.setText("Tebrikler! Bölümü Bitirdiniz :)")
                            self.bild.show()
                            self.fonk.pause_action()
                            self.bild.btn_next.setEnabled(False)
                            self.oyun.btn_sureDurdur.setEnabled(False)
                            self.butonPasif()

    def asagiGit(self,x,y):
        for i in self.oyun.btngrup.buttons():
            if i.x() == self.bosKonumX and i.y() < self.bosKonumY and i.y() >= y:
                i.setGeometry(i.x(),i.y() + self.yukseklik, self.genislik, self.yukseklik)

        self.bosKonumY = y
        self.bosKonumX = x



    def yukariGit(self,x,y):
        for i in self.oyun.btngrup.buttons():
            if i.x() == self.bosKonumX and i.y() > self.bosKonumY and i.y() <= y:
                i.setGeometry(i.x(), i.y() - self.yukseklik, self.genislik, self.yukseklik)

        self.bosKonumY = y
        self.bosKonumX = x

    def sagaGit(self,x,y):
        for i in self.oyun.btngrup.buttons():
            if i.y() == self.bosKonumY and i.x() < self.bosKonumX and i.x() >= x:
                i.setGeometry(i.x() + self.genislik, i.y(), self.genislik, self.yukseklik)

        self.bosKonumY = y
        self.bosKonumX = x

    def solaGit(self,x,y):
        for i in self.oyun.btngrup.buttons():
            if i.y() == self.bosKonumY and i.x() > self.bosKonumX and i.x() <= x:
                i.setGeometry(i.x() - self.genislik, i.y() , self.genislik, self.yukseklik)

        self.bosKonumY = y
        self.bosKonumX = x



    def hangiYon(self,i):
        if i.x() == self.bosKonumX and i.y() > self.bosKonumY:
            return "yukari"
        elif i.x() == self.bosKonumX and i.y() < self.bosKonumY:
            return "asagi"
        elif i.x() < self.bosKonumX and i.y() == self.bosKonumY:
            return "sag"
        else:
            return "sol"


    def satirSutunKontrol(self,i):
        if i.x() == self.bosKonumX or i.y() == self.bosKonumY:
            return True
        else:
            return False


    def butonPasif(self):
        for i in self.degisken.listButon:
            i.setEnabled(False)

    def butonAktif(self):
        for i in self.degisken.listButon:
            i.setEnabled(True)

    def bittimi(self):
        sayac = 0
        for i in range(self.degisken.boyut**2-1):

            buton = self.oyun.btngrup.button(i)
            X = self.genislik * (i % self.degisken.boyut)
            Y = self.yukseklik * int(i / self.degisken.boyut)


            if buton.x() == X and buton.y() == Y:
                sayac += 1

        if sayac == self.degisken.boyut**2-1:
            return True
        else:
            return False