from ortakfonksiyon import kart_numarasi_olustur, KAYIT_DOSYASI, konsolu_temizle , ccv_olustur ,tarih_olustur
from Banka.banka_giris_sayfasi import banka_giris_sayfasi
Bakiye = 0

def kayit_ol():
    konsolu_temizle()
    while True:
        # Ad kontrolü
        ad = input("Adınızı Giriniz: ") 
        if ad.isalpha() and len(ad) > 2:  
            soyad = input("Soyadınızı Giriniz: ")
            if soyad.isalpha():
                break  
            else:
                print("Soyadınızda Rakam , Özel Karakter Ve 3 Harften Az Olamaz. Lütfen Tekrar Deneyiniz.")
        else:
            print("Adınızda Rakam veya Özel Karakter Olamaz. Lütfen Tekrar Deneyiniz.")

    while True:
        # TC kimlik numarası kontrolü
        tc = input("Tc Kimlik Numaranızı Giriniz: ")
        if tc.isdigit() and len(tc) == 11:
            break
        else:
            print("Geçersiz TC Kimlik Numarası! 11 Haneli Rakamdan Oluşmak Zorundadır.")

    while True:
        # Şifre kontrolü
        sifre = input("Şifrenizi Giriniz: ")
        if sifre.isdigit() and len(sifre) >= 6:
            break
        else:
            print("Şifre en az 6 Rakamdan Oluşmalıdır!")         

    kart_numarasi = kart_numarasi_olustur()
    ccv_numarasi = ccv_olustur()
    tarih_numarasi = tarih_olustur()

    # Vadesiz hesap bakiyesi otomatik 1000, kredi kartı bakiyesi ise sıfır
    vadesiz_bakiye = 1000
    kredi_karti_bakiye = 0

    # Yeni alan: Kart durumu başlangıçta pasif (0)
    kart_durumu = "0"

    with open(KAYIT_DOSYASI, "a") as dosya:
        dosya.write(f"{tc},{sifre},{kart_numarasi},{ccv_numarasi},{tarih_numarasi},{vadesiz_bakiye},{kredi_karti_bakiye},{kart_durumu}\n")

    input("Devam Etmek İçin Lütfen Enter'a Basınız. ")
    konsolu_temizle()