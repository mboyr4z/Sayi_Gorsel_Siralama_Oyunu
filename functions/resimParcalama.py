import cv2

def parcala(konum,boyut):
    resim=cv2.imread(konum)
    resim = cv2.resize(resim, (450, 380))

    yukseklik, genislik = resim.shape[0], resim.shape[1]

    parca_genislik, parca_yukseklik = int(genislik / boyut), int(yukseklik / boyut)

    x, y = 0, 0
    sayac=0
    for i in range(0,boyut):
        for j in range(0, boyut):
            img = resim[y: y + parca_yukseklik, x: x + parca_genislik]
            cv2.imwrite("../functions/parcaliResimler/"+str(sayac)+".jpg",img)
            sayac+=1
            x += parca_genislik
        x = 0
        y += parca_yukseklik