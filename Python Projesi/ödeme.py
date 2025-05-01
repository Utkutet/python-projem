import datetime
from ortakfonksiyon import KAYIT_DOSYASI, konsolu_temizle
from Market.market_islemleri import sepet_toplam_tutari
import os
from Market.market_giris import giris_yapan_kullanici


def geçmiş_satın_alımları_kaydet(ad, sepet):
    # Kullanıcı adına dosya oluştur
    dosya_adi = f"satın_alımlar/{ad}_satın_alımlar.txt"  # Kullanıcı adıyla dosya
    os.makedirs("satın_alımlar", exist_ok=True)  # Klasörü oluştur

    # Sepeti dosyaya kaydet
    with open(dosya_adi, "a") as dosya:
        for ürün in sepet:
            satır = f"{datetime.datetime.now()} - {ürün['isim']} - {ürün['fiyat']} TL - {ürün['miktar']} adet\n"
            dosya.write(satır)


def bildirim_ekle(tc, tutar, detay):
    bildirim = f"[{datetime.datetime.now()}] - {tc} - {tutar:.2f} TL - {detay}\n"
    with open("bildirimler.txt", "a") as dosya:
        dosya.write(bildirim)

# Ödeme fonksiyonu
def ödeme(sepet):
    global giris_yapan_kullanici #Değişkenin değerini alıyor böylece sepeti ada göre kaydediyor.
    # Kullanıcı verilerini dosyadan okuma
    try:
        # BANKA KAYIT BİLGİLERİNİ OKUYOR KART BİLGİLERİNİ KONTROL ETMEK İÇİN
        with open(KAYIT_DOSYASI, "r") as dosya:
            kayıtlar = [satir.strip().split(",") for satir in dosya if satir.strip()]

        # Kullanıcıdan bilgileri al
        numara = input("Kart Numaranızı Giriniz: ")
        eşleşen_kayıt = None  # Eşleşen kaydı saklamak için

        # Tüm kayıtlarla karşılaştır
        for veri in kayıtlar:
            if len(veri) == 8:  # Veri formatının doğru olduğundan emin ol
                kayitli_tc, kayitli_sifre, kayitli_kart_numarasi, kayitli_ccv_numarasi, kayitli_tarih_numarasi, kayitli_vadesiz_bakiye, kayitli_kredi_karti_bakiye, kart_durumu = veri

                # Kart numarasını kontrol et
                if numara == kayitli_kart_numarasi:
                    if kart_durumu == "0":
                        print("Bu kart pasif durumda. Lütfen önce kartı aktif hale getirin.")
                        return

                    Şifre = input("Şifrenizi Giriniz: ")
                    if Şifre == kayitli_sifre:
                        ccv = input("CCV Numaranızı Giriniz: ")
                        if ccv == kayitli_ccv_numarasi:
                            SonKullanma = input("Son Kullanım Tarihini Giriniz: ")
                            if SonKullanma == kayitli_tarih_numarasi:
                                eşleşen_kayıt = veri
                                break  # İlk eşleşmede döngüyü bitir
                            else:
                                print("Son Kullanma Tarihi Yanlıştır.")
                        else:
                            print("CCV numarası yanlış.")
                    else:
                        print("Şifre yanlış.")

        # Sonuçları değerlendir
        if eşleşen_kayıt:
            # Sepet tutarını market işlemlerinden çekelim
            try:
                sepet_tutari = sepet_toplam_tutari(sepet)
                kayitli_kredi_karti_bakiye = float(kayitli_kredi_karti_bakiye)

                if sepet_tutari > kayitli_kredi_karti_bakiye:
                    print("Yetersiz bakiye! Ödeme gerçekleştirilemedi.")
                    return

                kayitli_kredi_karti_bakiye -= sepet_tutari

                print("Ödeme Başarılı!")
                print(f"Kalan Bakiye: {kayitli_kredi_karti_bakiye:.2f} TL")
                bildirim_ekle(kayitli_tc, sepet_tutari, "Market alışverişi")
                geçmiş_satın_alımları_kaydet(giris_yapan_kullanici, sepet)
                input()

                # Bakiye güncelleme
                with open(KAYIT_DOSYASI, "r") as dosya:
                    satirlar = dosya.readlines()

                with open(KAYIT_DOSYASI, "w") as dosya:
                    for satir in satirlar:
                        veri = satir.strip().split(",")
                        if len(veri) == 8 and veri[0] == kayitli_tc:
                            veri[6] = f"{int(kayitli_kredi_karti_bakiye)}"
                            dosya.write(",".join(veri) + "\n")
                        else:
                            dosya.write(satir)

                    konsolu_temizle()
                    from Market.market_islemleri import market_islemleri
                    market_islemleri()

            except ValueError:
                print("Geçersiz sepet tutarı. İşlem iptal edildi.")
        else:
            print("Girdiğiniz bilgilerle eşleşen bir kayıt bulunamadı.")

    except FileNotFoundError:
        print(f"Dosya bulunamadı: {KAYIT_DOSYASI}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")