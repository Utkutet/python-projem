import os
from ortakfonksiyon import kart_numarasi_olustur, KAYIT_DOSYASI, konsolu_temizle , ccv_olustur ,tarih_olustur
from Market.market_islemleri import sepet_toplam_tutari
def kart_ayarlari(tc):
    with open(KAYIT_DOSYASI, "r") as dosya:
        satirlar = dosya.readlines()

    yeni_satirlar = []
    kart_durumu = None

    for satir in satirlar:
        veri = satir.strip().split(",")
        if len(veri) == 8 and veri[0] == tc:
            kart_durumu = veri[7]  # Mevcut kart durumu
            break

    if kart_durumu is None:
        print("Kart bilgileri bulunamadı. Lütfen tekrar deneyin.")
        return

    print(f"Kart Durumu: {'Aktif' if kart_durumu == '1' else 'Pasif'}")
    while True:
        print("\n1-) Kartı Aktif Et")
        print("2-) Kartı Pasif Duruma Getir")
        print("3-) Geri")
        secim = input("\nSeçiminizi Yapınız: ")

        if secim == "1":
            if kart_durumu == "1":
                print("Bu kart zaten aktif durumda.")
            else:
                kart_durumu = "1"
                print("Kart aktif hale getirildi.")
        elif secim == "2":
            if kart_durumu == "0":
                print("Bu kart zaten pasif durumda.")
            else:
                kart_durumu = "0"
                print("Kart pasif hale getirildi.")
        elif secim == "3":
            konsolu_temizle()
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")

    for satir in satirlar:
        veri = satir.strip().split(",")
        if len(veri) == 8 and veri[0] == tc:
            veri[7] = kart_durumu
            yeni_satirlar.append(",".join(veri))
        else:
            yeni_satirlar.append(satir.strip())

    with open(KAYIT_DOSYASI, "w") as dosya:
        dosya.write("\n".join(yeni_satirlar) + "\n")

def Kartlar(tc):
    if not os.path.exists(KAYIT_DOSYASI):
        print("Kayıt dosyası bulunamadı!")
        return

    with open(KAYIT_DOSYASI, "r") as dosya:
        for satir in dosya:
            satir = satir.strip()  # Satır başı ve sonu boşlukları temizle
            veri = satir.split(",")  # Virgülle ayır

            if len(veri) == 8:
                kayitli_tc, _, kart_numarasi, ccv_numarasi, tarih_numarasi, _, _, kart_durumu = veri
                if kayitli_tc == tc:
                    # Kart numarasını her 4 hanede bir boşluk koyarak formatla
                    formatli_kart_numarasi = " ".join(
                        kart_numarasi[i:i+4] for i in range(0, len(kart_numarasi), 4)
                    )

                    while True:
                        print("+--------------------+---------------------+")
                        print("| Bilgi Türü          | Detaylar           |")
                        print("+--------------------+---------------------+")
                        print(f"| Kart Numarası       | {formatli_kart_numarasi}|")
                        print(f"| CCV                 | {ccv_numarasi}                |")
                        print(f"| Son Kullanma Tarihi | {tarih_numarasi}              |")
                        print("+--------------------+---------------------+")

                        print("\n1-) Karta Bakiye Yükle")
                        print("2-) Kart Ayarları")
                        print("3-) Geri")
                        secim = input("\nSeçiminizi Yapınız: ")

                        if secim == "1":
                            miktar = input("Yüklemek istediğiniz miktarı giriniz: ")
                            if miktar.isdigit():
                                miktar = int(miktar)
                                yeni_satirlar = []
                                konsolu_temizle()

                                with open(KAYIT_DOSYASI, "r") as dosya:
                                    for satir in dosya:
                                        satir = satir.strip()
                                        veri = satir.split(",")
                                        if len(veri) == 8:
                                            kayitli_tc, sifre, kart_numarasi, ccv_numarasi, tarih_numarasi, vadesiz_bakiye, kredi_karti_bakiye, kart_durumu = veri
                                            if kayitli_tc == tc:
                                                vadesiz_bakiye = int(vadesiz_bakiye)
                                                kredi_karti_bakiye = int(kredi_karti_bakiye)

                                                if miktar > vadesiz_bakiye:
                                                    print("Yetersiz bakiye! İşlem gerçekleştirilemedi.")
                                                else:
                                                    vadesiz_bakiye -= miktar
                                                    kredi_karti_bakiye += miktar
                                                    print(f"{miktar} TL kredi kartınıza başarıyla yüklendi!")

                                                veri[5] = str(vadesiz_bakiye)
                                                veri[6] = str(kredi_karti_bakiye)

                                        yeni_satirlar.append(",".join(veri))

                                with open(KAYIT_DOSYASI, "w") as dosya:
                                    dosya.write("\n".join(yeni_satirlar) + "\n")

                            else:
                                print("Geçersiz miktar girdiniz.")

                        elif secim == "2":  # Kart Ayarları
                            kart_ayarlari(tc)
                        elif secim == "3":
                            return
                        else:
                            print("\nGeçersiz seçim. Lütfen tekrar deneyin.")
                        input("\nDevam etmek için Enter'a basınız...")
                        konsolu_temizle()

                    return

    print("Kart bilgileri bulunamadı. Lütfen tekrar deneyiniz.")