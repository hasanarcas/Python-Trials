aSaniyeAdım = float(input("A kaplumbağasının saat başına adım sayısını giriniz :")) / 3600
bSaniyeAdım = float(input("B kaplumbağasının saat başına adım sayısını giriniz :")) /3600
z = int(input("A yarışa başadığı zaman B'nin adım uzaklığı :"))
if bSaniyeAdım < aSaniyeAdım:
    aKonum = 0
    bKonum = z
    gecenSaniye = -1
    while(aKonum < bKonum):
        gecenSaniye +=1
        aKonum += aSaniyeAdım
        bKonum += bSaniyeAdım
    saniye = (gecenSaniye % 60)
    dakika = (gecenSaniye // 60) % 60
    saat = gecenSaniye // 3600
    print(saat , dakika , saniye)
if aSaniyeAdım < bSaniyeAdım:
    print(-1,-1,-1)