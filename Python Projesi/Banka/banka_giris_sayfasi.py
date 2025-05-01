import time
from deneme import banka_giris_mesajı

def banka_giris_sayfasi():
    while True:
        banka_giris_mesajı()
        print("\n1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Ana Menüye Dön")

        # Kullanıcıdan giriş alıyoruz ve hemen int'e çevirmeye çalışıyoruz
        secim = input("Seçim Yapınız: ")

        # Burada sayıyı kontrol edip, geçerli bir giriş yapılıp yapılmadığını kontrol ediyoruz
        if secim.isdigit():  # Eğer girilen değer tamamen sayılardan oluşuyorsa
            secim = int(secim)  # Sayıya dönüştür
            if secim == 1:
                from Banka.kayit import kayit_ol
                kayit_ol()
                break
            elif secim == 2:
                from Banka.kullanici_giris import giris_yap
                giris_yap()
                break
            elif secim == 3:
                from Anamenu import anamenu
                anamenu()  # Ana menüye dönüş
                break
            else:
                print("Geçersiz Seçim. Lütfen Tekrar Deneyiniz")
        else:
            print("Lütfen Sayı Giriniz.")  # Eğer kullanıcı sayı dışında bir şey girerse