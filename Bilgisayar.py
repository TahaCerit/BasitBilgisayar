import time
import random
class Bilgisayar():
    def __init__(self,marka = "Lenovo",işlemci = "Intel Core i5",bilgisayar_durumu = "Kapalı",bilgisayar_ses = 0,wifi_listesi = ["Ceritoğlu Malikanesi","Şen Malikanesi"],internet = "Ceritoğu Malikanesi"):
        self.marka = marka
        self.işlemci = işlemci
        self.bilgisayar_durumu = bilgisayar_durumu
        self.bilgisayar_ses = bilgisayar_ses
        self.wifi_listesi =wifi_listesi
        self.internet = internet
    def ses_aç_kapa (self):
        while True:
            seviye = input("Sesi Açmak İçin '+' Azaltmak İçin '-' Tamamlamak için Herhani bir Tuşa basın..")
            if (seviye == "+"):
                if(self.bilgisayar_ses !=10):
                    self.bilgisayar_ses += 1
                    print("Sesi:",self.bilgisayar_ses)
            elif (seviye == "-"):
                if(self.bilgisayar_ses !=0):
                    self.bilgisayar_ses -= 1
                    print("Sesi:",self.bilgisayar_ses)
            else:
                print("Bilgisayarın Sesi Güncelleniyor...")
                time.sleep(1)
                break
    def pc_aç (self):
        print("Bilgisayarınız Açılıyor...")
        time.sleep(1)
        print("Hoşgeldiniz..\nNasıl Yardımcı Olabilirim?")
        time.sleep(1)
        self.bilgisayar_durumu = "Açık"
    def pc_kapat(self):
        print("Bilgisayarınız Kapanıyor...")
        time.sleep(1)
        print("Güle Güle Gene Bekleriz... ;)")
        time.sleep(1)
        self.bilgisayar_durumu = "Kapalı"
    def __len__(self):
        return len(self.wifi_listesi)
    def açık_wifi(self):
        açık = random.randint(0,len(self.wifi_listesi)-1)
        self.internet =self.wifi_listesi[açık]
        time.sleep(1)
        print("İnternete Bağlandınız:",self.internet)
    def __str__(self):
        return "\nBilgisayar Durumunuz: {}\nSes Düzeyi: {}\nİnternet: {}\nMarkası: {}\nİşlemcisi: {}\n".format(self.bilgisayar_durumu,self.bilgisayar_ses,self.internet,self.marka,self.işlemci)
    def wifi_ekle(self,internet):
        time.sleep(1)
        print("Yeni Wifi Ağı Eklendi..",internet)
        self.wifi_listesi.append(internet)
bilgisayar = Bilgisayar()

ekran ="LENOVO DİZÜSTÜ BİLGİSAYARI"
print("*"*len(ekran),ekran,"*"*len(ekran),sep="\n")

açma =input("Bilgisayarı Açmak İçin 'w' ya basın...:")
if(açma == "w"):
    bilgisayar.pc_aç()
print("""
**************************
LENOVE DİZÜSTÜ BİLGİSAYARI
**************************

        İŞLEMLERİM
        **********
1-Bilgisayar Özellikleri

2-Ses Düzeyini Ayarla

3-Wifi Aç-Kapa

4-Yeni Wifi Ağı Ekle

5-Bilgisayarı Kapat


""")

while True:
    işlemler = input("Sana NasıL Yardımıcı Olurum?\n\nBir İşlem Seçin:")
    if (işlemler == "1"):
        print(bilgisayar)
    elif(işlemler == "2"):
        bilgisayar.ses_aç_kapa()
    elif(işlemler == "3"):
        bilgisayar.açık_wifi()
    elif(işlemler == "4"):
        ağlar = input("Yeni Bir WiFi Ağı Yazınız:")
        eklenecek = ağlar.split(",")
        for i in eklenecek:
            bilgisayar.wifi_ekle(i)
    elif (işlemler =="5"):
        bilgisayar.pc_kapat()
        break
    else:
        print("Geçersiz İşlem..")