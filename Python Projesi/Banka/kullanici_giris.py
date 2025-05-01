import time
import os
from ortakfonksiyon import KAYIT_DOSYASI, konsolu_temizle
from Banka.banka_ana_menu import banka_ana_menu
from deneme import yüklemeekranı

def giris_yap():
    konsolu_temizle()

    if not os.path.exists(KAYIT_DOSYASI):
        print("Kaydınız Bulunamadı... Lütfen Önce Kayıt Olunuz!")
        return

    while True:
        print("Giriş ekranından çıkmak için '0' tuşlayabilirsiniz.")
        tc = input("Tc Kimlik Numaranızı Giriniz: ")
        if tc == "0":
            print("Ana menüye dönülüyor...")
            time.sleep(2)
            konsolu_temizle()
            return
        if tc.isdigit() and len(tc) == 11:  # TC Kimlik numarası kontrolü
            sifre = input("6 Haneli Şifrenizi Giriniz: ")
            if sifre == "0":
                print("Ana menüye dönülüyor...")
                time.sleep(2)
                konsolu_temizle()
                return
            if sifre.isdigit() and len(sifre) == 6:  # Şifre kontrolü
                with open(KAYIT_DOSYASI, "r") as dosya:
                    for satir in dosya:
                        # Satırdaki boşlukları temizliyoruz ve virgüllere göre ayırıyoruz
                        satir = satir.strip()  # Satır başı ve sonu boşlukları temizle
                        veri = satir.split(",")  # Virgülle ayır

                        # Satır formatı doğruysa işleme devam et
                        if len(veri) == 8:
                            kayitli_tc, kayitli_sifre, _, _, _, _, _, _ = veri
                            if tc == kayitli_tc and sifre == kayitli_sifre:  # Giriş doğrulaması
                                konsolu_temizle()
                                yüklemeekranı(4) #animasyon geldi
                                print("\nGiriş tamamlandı!") #animasyon tamamlanır tamamlanmaz bu geldi
                                time.sleep(2) #2 saniye bekliyoruz
                                banka_ana_menu(tc)  # TC'yi menüye geçiyoruz
                                return
                konsolu_temizle()
                yüklemeekranı(4)
                print("\nHatalı TC veya Şifre! Lütfen Tekrar Deneyiniz.")
                input("Devam etmek için lütfen enter'a basınız...")
                konsolu_temizle()
            else:
                konsolu_temizle()
                print("Şifreniz 6 Haneli Rakamdan Oluşmalıdır.")
        else:
            konsolu_temizle()
            print("TC Kimlik Numarası 11 Haneli Rakamdan Oluşmak Zorundadır.")