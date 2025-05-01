import time

from ortakfonksiyon import konsolu_temizle
from indirim_kuponu import INDIRIM_KUPONU
import os
from Market.market_giris import giris_yapan_kullanici

def sepet_toplam_tutari(sepet):
    return sum(ürün['fiyat'] * ürün['miktar'] for ürün in sepet)

def market_islemleri():
    from ortakfonksiyon import konsolu_temizle
    from ürün_listesi import kategori_getir

    sepet = []

    while True:
        print("---- Kategoriler ----")
        print("1-) Yiyecek")
        print("2-) İçecek")
        print("3-) Eşyalar")
        print("4-) Sepeti Görüntüle")
        print("5-) İndirim Kodu İçin Tek Seferlik Oyun Oyna")
        print("6-) Geçmiş Satın Alımları Görüntüle")
        print("7-) Çıkış Yap ")

        try:
            secim = int(input("Seçim Yapınız: "))

            if secim == 1:
                konsolu_temizle()
                ürünler = kategori_getir("yiyecekler")
                if ürünler:  # Eğer ürünler boş değilse
                    print("---- Yiyecekler ----")
                    for i, ürün in enumerate(ürünler, 1):
                        print(f"{i}. {ürün['isim']} - {ürün['fiyat']} TL")
                    ürün_sec = int(input("Sepete eklemek için ürün numarasını giriniz (0: İptal): "))
                    if 0 < ürün_sec <= len(ürünler):
                        miktar = int(input("Kaç adet eklemek istiyorsunuz?: "))
                        if miktar > 0:
                            ürün = ürünler[ürün_sec - 1]
                            sepet.append({"isim": ürün['isim'], "fiyat": ürün['fiyat'], "miktar": miktar})
                            print(f"{ürün['isim']} sepete {miktar} adet eklendi.")
                            time.sleep(2)
                            konsolu_temizle()
                        else:
                            print("Geçersiz miktar. İşlem iptal edildi.")
                    elif ürün_sec == 0:
                        print("İptal edildi.")
                    else:
                        print("Geçersiz seçim.")
                else:
                    print("Bu kategoride ürün bulunmamaktadır.")

            elif secim == 2:
                konsolu_temizle()
                ürünler = kategori_getir("içecekler")
                if ürünler:  # Eğer ürünler boş değilse
                    print("---- İçecekler ----")
                    for i, ürün in enumerate(ürünler, 1):
                        print(f"{i}. {ürün['isim']} - {ürün['fiyat']} TL")
                    ürün_sec = int(input("Sepete eklemek için ürün numarasını giriniz (0: İptal): "))
                    if 0 < ürün_sec <= len(ürünler):
                        miktar = int(input("Kaç adet eklemek istiyorsunuz?: "))
                        if miktar > 0:
                            ürün = ürünler[ürün_sec - 1]
                            sepet.append({"isim": ürün['isim'], "fiyat": ürün['fiyat'], "miktar": miktar})
                            print(f"{ürün['isim']} sepete {miktar} adet eklendi.")
                            time.sleep(2)
                            konsolu_temizle()
                        else:
                            print("Geçersiz miktar. İşlem iptal edildi.")
                    elif ürün_sec == 0:
                        print("İptal edildi.")
                    else:
                        print("Geçersiz seçim.")
                else:
                    print("Bu kategoride ürün bulunmamaktadır.")

            elif secim == 3:
                konsolu_temizle()
                ürünler = kategori_getir("eşyalar")
                if ürünler:  # Eğer ürünler boş değilse
                    print("---- Eşyalar ----")
                    for i, ürün in enumerate(ürünler, 1):
                        print(f"{i}. {ürün['isim']} - {ürün['fiyat']} TL")
                    ürün_sec = int(input("Sepete eklemek için ürün numarasını giriniz (0: İptal): "))
                    if 0 < ürün_sec <= len(ürünler):
                        miktar = int(input("Kaç adet eklemek istiyorsunuz?: "))
                        if miktar > 0:
                            ürün = ürünler[ürün_sec - 1]
                            sepet.append({"isim": ürün['isim'], "fiyat": ürün['fiyat'], "miktar": miktar})
                            print(f"{ürün['isim']} sepete {miktar} adet eklendi.")
                            time.sleep(2)
                            konsolu_temizle()
                        else:
                            print("Geçersiz miktar. İşlem iptal edildi.")
                    elif ürün_sec == 0:
                        print("İptal edildi.")
                    else:
                        print("Geçersiz seçim.")
                else:
                    print("Bu kategoride ürün bulunmamaktadır.")

            elif secim == 4:
                if not sepet:
                    print("Sepetiniz boş.")
                else:
                    while True:
                        print("--- Sepetiniz ---")
                        toplam = 0
                        for i, ürün in enumerate(sepet, 1):
                            toplam += ürün['fiyat'] * ürün['miktar']
                            print(f"{i}. {ürün['isim']} - {ürün['fiyat']} TL x {ürün['miktar']} adet")
                        print(f"Toplam: {toplam} TL")
                        print("1-) Sepetten ürün çıkar")
                        print("2-) Ödemeye Geç")
                        print("3-) İndirim Kuponu Gir")
                        print("4-) Geri Git")

                        try:
                            secim_sepet = int(input("Seçim yapınız: "))
                            if secim_sepet == 1:
                                ürün_cikar = int(input("Çıkarmak istediğiniz ürünün numarasını giriniz (0: İptal): "))
                                if 0 < ürün_cikar <= len(sepet):
                                    miktar_cikar = int(input("Kaç adet çıkarmak istiyorsunuz?: "))
                                    if 0 < miktar_cikar <= sepet[ürün_cikar - 1]['miktar']:
                                        sepet[ürün_cikar - 1]['miktar'] -= miktar_cikar
                                        print(
                                            f"{miktar_cikar} adet {sepet[ürün_cikar - 1]['isim']} sepetten çıkarıldı.")
                                        if sepet[ürün_cikar - 1]['miktar'] == 0:
                                            sepet.pop(ürün_cikar - 1)
                                    else:
                                        print("Geçersiz miktar. İşlem iptal edildi.")
                                elif ürün_cikar == 0:
                                    print("İptal edildi.")
                                else:
                                    print("Geçersiz seçim.")
                            elif secim_sepet == 2:
                                toplam = sum(ürün['fiyat'] * ürün['miktar'] for ürün in sepet)
                                if toplam <= 0:
                                    print("Toplam sepet tutarı 0'ın altında olamaz. Ödemeye geçilemiyor.")
                                else:
                                    from ödeme import ödeme
                                    ödeme(sepet)
                            elif secim_sepet == 3:  # İndirim Kuponu Gir
                                print("İndirim Kuponu Uygula")
                                kupon = input("İndirim Kodunuzu Giriniz: ").strip()
                                try:
                                    with open("indirim_kuponu.txt", "r") as dosya:
                                        mevcut_kuponlar = [k.strip() for k in dosya.readlines()]
                                    if kupon in mevcut_kuponlar:
                                        print("Kupon doğru! Sepete 200 TL indirim uygulandı.")

                                        # İndirim uygulandıktan sonra toplam tutarı kaydet
                                        sepet.append({"isim": "İndirim Kuponu", "fiyat": -200, "miktar": 1})

                                        # Kullanılan kuponu dosyadan sil
                                        mevcut_kuponlar.remove(kupon)
                                        with open("indirim_kuponu.txt", "w") as dosya:
                                            for kalan_kupon in mevcut_kuponlar:
                                                dosya.write(kalan_kupon + "\n")
                                        print("Kupon artık kullanılamaz hale getirildi.")
                                    else:
                                        print("Geçersiz kupon. Lütfen tekrar deneyin.")
                                except FileNotFoundError:
                                    print("İndirim kuponu listesine ulaşılamıyor.")
                                except Exception as e:
                                    print(f"Bir hata oluştu: {e}")
                            elif secim_sepet == 4:
                                break
                            else:
                                print("Geçersiz seçim.")
                        except ValueError:
                            print("Geçerli bir sayı giriniz.")

            elif secim==5:
                konsolu_temizle()
                from indirim_kuponu import indirim
                indirim()
                input("Devam etmek için Enter'a basınız...")
                konsolu_temizle()


            elif secim==6:
                konsolu_temizle()
                # Geçmiş satın alımları görüntüleme
                dosya_adi = f"satın_alımlar/{giris_yapan_kullanici}_satın_alımlar.txt"
                if os.path.exists(dosya_adi):
                    with open(dosya_adi, "r") as dosya:
                        print("--- Geçmiş Satın Alımlarınız ---")
                        print(dosya.read())
                        input("Devam etmek için Enter'a basınız...")
                        konsolu_temizle()
                else:
                    print("Henüz bir satın alım geçmişiniz bulunmamaktadır.")
                    input("Devam etmek için Enter'a basınız...")

            elif secim == 7:
                konsolu_temizle()
                break
            else:
                print("Geçersiz seçim!")
        except ValueError:
                print("Geçerli bir sayı giriniz.")