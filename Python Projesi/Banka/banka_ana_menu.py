import time
from ortakfonksiyon import konsolu_temizle
from ortakfonksiyon import kart_numarasi_olustur, KAYIT_DOSYASI, konsolu_temizle , ccv_olustur ,tarih_olustur
from Anamenu import anamenu

def bildirimleri_goster(tc):
    try:
        with open("bildirimler.txt", "r") as dosya:
            bildirimler = dosya.readlines()

        kullanici_bildirimleri = [b for b in bildirimler if f"- {tc} -" in b]

        if kullanici_bildirimleri:
            print("--- Bildirimleriniz ---")
            for bildirim in kullanici_bildirimleri:
                print(bildirim.strip())
        else:
            print("Hiç bir bildiriminiz yok.")
    except FileNotFoundError:
        print("Bildirim dosyası bulunamadı.")


def banka_ana_menu(tc):
    konsolu_temizle()
     
    # İlk başta bakiye bilgisi None olarak tanımlanıyor
    vadesiz_bakiye = None

    while True:
        konsolu_temizle()

        # Dosyayı açıp, kullanıcının TC'sine ait bakiyeyi bulalım
        with open(KAYIT_DOSYASI, "r") as dosya:
            for satir in dosya:
                satir = satir.strip()  # Satır başı ve sonu boşlukları temizle
                veri = satir.split(",")  # Virgülle ayır

                if len(veri) == 8:
                    kayitli_tc, _, kart_numarasi, ccv_numarasi, tarih_numarasi, vadesiz_bakiye, kredi_karti_bakiye, kart_durumu = veri
                    
                    # Eğer TC'ler eşleşirse, bakiye bilgisini al
                    if kayitli_tc == tc:
                        break  # TC bulundu, döngüyü sonlandır

        # Eğer TC bulunamadıysa, kullanıcıya mesaj göster
        if vadesiz_bakiye is None:
            print("Bu TC ile kayıta ulaşılamadı.")
            input("\nDevam etmek için Enter'a basınız...")
            continue

        # Bakiye bulunduysa, ana menüyü göster
        konsolu_temizle()
        print("+--------------------------------+")
        print(f"|Vadesiz Hesap Bakiyesi: {vadesiz_bakiye} TL  |")
        print("+--------------------------------+")
        print("\n1-) Kartlarım")
        print("2-) Bildirimler")
        print("3-) Çıkış Yap")

        secim = input("\nSeçiminizi Yapınız: ")

        if secim == "1":
            konsolu_temizle()
            from Banka.Kartlar import Kartlar
            Kartlar(tc)  # Kullanıcının TC'sini gönderiyoruz
        elif secim == "2":
            konsolu_temizle()
            bildirimleri_goster(tc)
        elif secim == "3":
            anamenu()
        else:
            print("\nGeçersiz seçim. Lütfen tekrar deneyin.")
        input("\nDevam etmek için Enter'a basınız...")