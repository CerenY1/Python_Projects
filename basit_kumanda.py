
import random
import time

class Kumanda():

    def __init__(self,tv_durumu="Kapalı",ses_durumu=0,kanal_listesi=["Trt"],kanal="Trt",parlaklık_durumu=50):

        self.tv_durumu = tv_durumu
        self.ses_durumu = ses_durumu
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.parlaklık_durumu = parlaklık_durumu

    def tv_aç(self):

       if self.tv_durumu == "Açık":
           print("Televizyon zaten açık...")

       else:
           print("Televizyon açılıyor...")
           self.tv_durumu="Açık"

    def tv_kapat(self):

        if self.tv_durumu == "Kapalı":
            print("Televizyon zaten kapalı...")

        else:
            print("televizyon kapatılıyor...")
            self.tv_durumu="Kapalı"

    def ses_ayarları(self):

        while True:

            ses = input("Sesi yükseltmek için :> \n tuşuna azaltmak için :< tuşuna basınız.")
            if ses =="<":
                if self.ses_durumu!=0:
                   self.ses_durumu-=1
                   print("Ses:",self.ses_durumu)


            elif ses == ">":
                if self.ses_durumu!=31:
                    self.ses_durumu+=1
                    print("Ses:",self.ses_durumu)

            else:
                print("Güncel ses:",self.ses_durumu)

                break

    def kanal_ekle(self,kanal_ismi):


         print("Kanallar güncelleniyor...")
         time.sleep(1)
         self.kanal_listesi.append(kanal_ismi)
         print("Kanal eklendi...")

    def kanallar(self):
        print("Güncel Kanal Listesi: ",self.kanal_listesi)

    def rastgele_kanal(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]

        print("Kanal:",self.kanal)

    def parlaklık(self):

        while True:

          parlak = input("Parlaklığı artırmak için '+' tuşuna,azaltmak için '-' tuşuna basınız.\nParlaklık:")

          if parlak=="+":
              if self.parlaklık_durumu != 100:
                 self.parlaklık_durumu += 10
                 print("Parlaklık artırılıyor...")
                 time.sleep(1)
                 print("Güncel Parlaklık:%{}".format(self.parlaklık_durumu))


          elif parlak == "-":
              if self.parlaklık_durumu != 0:
                 self.parlaklık_durumu -= 10
                 print("Parlaklık azaltılıyor...")
                 time.sleep(1)
                 print("Güncel Parlaklık:%{}".format(self.parlaklık_durumu))

          else:
               print("Geçersiz işlem...")
               break


    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu:{} \n Ses Durumu:{} \n Kanal:{} \n Kanal Listesi:{} \n Parlaklık:{}".format(self.tv_durumu,self.ses_durumu,self.kanal,self.kanal_listesi,self.parlaklık_durumu)

kumanda=Kumanda()

print("""
Kumanda Uygulaması

1)Tv aç
2)Tv kapat
3)Ses ayarları
4)Kanal ekleme
5)Kanal sayısı
6)Kanal listesi
7)Rastgele kanala geçme
8)Parlaklık durumu
9)Televizyon bilgileri

"""

)

while True:
    işlem = int(input("İşlem:"))

    if işlem==1:
        kumanda.tv_aç()

    elif işlem==2:
        kumanda.tv_kapat()

    elif işlem==3:
        kumanda.ses_ayarları()

    elif işlem==4:
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem==5:
        print("Kanal Sayısı:",len(kumanda))

    elif işlem==6:
        kumanda.kanallar()

    elif işlem==7:
        kumanda.rastgele_kanal()

    elif işlem==8:
        kumanda.parlaklık()

    elif işlem==9:
        print(kumanda)

    else:
        print("Geçersiz işlem...")



















