from PyQt5 import QtWidgets
import sys
import os
from SayiSiralama.design import Anasayfa,oyunekrani,bildirim,egitim
from SayiSiralama.functions import fonksiyonlar,degiskenler,algoritma

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    os.chdir("./design")

    ana = Anasayfa.Ui_anaekran()
    ana.setupUi()

    oyun = oyunekrani.Ui_Oyunekrani()
    oyun.setupUi()

    bild = bildirim.Ui_bildirim()
    bild.setupUi()

    egitim=egitim.Ui_Egitim()
    egitim.setupUi()

    degisken=degiskenler.degisken()

    alg = algoritma.algoritma()
    fonk = fonksiyonlar.function()

    alg.constructure(ana, oyun, bild, egitim, degisken,fonk)
    fonk.sayfaGecisi(ana,oyun,bild,egitim,degisken,alg)
    ana.goster()

    sys.exit(app.exec())