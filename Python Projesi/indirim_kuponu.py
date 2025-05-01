from ortakfonksiyon import INDIRIM_KUPONU
import random
import string
from datetime import datetime, timedelta

sayi = random.randint(1,3) #denemek kolay olsun diye 1 ile 3 arasında bir sayı atıyoruz.
oyun_oynandı = False
oynama_zamanı = None

def indirim():
    global oyun_oynandı, oynama_zamanı

    #daha önce oynandımı diye kontrol ediyoruz
    if oyun_oynandı and oynama_zamanı:
        kalan_süre = (oynama_zamanı + timedelta(hours=24)) - datetime.now()
        if kalan_süre.total_seconds() > 0:
            kalan_saat = kalan_süre.seconds // 3600
            kalan_dakika = (kalan_süre.seconds % 3600) // 60
            kalan_saniye = kalan_süre.seconds % 60
            print(f"Bu oyunu son 24 saat içinde oynadınız. "
                  f"Lütfen {kalan_saat} saat, {kalan_dakika} dakika, {kalan_saniye} saniye sonra tekrar deneyiniz.")
            return


    print("Tahmin oyununa hoşgelidniz...")
    print("Eğer sayıyı doğru tahmin ederseniz 200 tllik indirim kuponu kazanacaksınız.")

    tahmin = int(input("1-50 arasında olan sayıyı tahmin ediniz: "))
    if tahmin == sayi:
        print("TEBRİKLER KAZANDINIZ!")
        oyun_oynandı = True  # Oyun oynandı olarak işaretle
        oynama_zamanı = datetime.now()
        kupon = indirim_kuponu_olusturucu()
        print(f"İndirim Kuponunuz: {kupon}")
        with open(INDIRIM_KUPONU, "a") as dosya:
            dosya.write(f"{kupon}\n")

    else:
        oyun_oynandı = True
        oynama_zamanı = datetime.now()
        print("Üzgünüz, doğru tahmin edemediniz. Yarın tekrar deneyiniz.")
        print(f"Doğru sayı: {sayi}")

def indirim_kuponu_olusturucu(uzunluk=5):
    karakterler = string.ascii_uppercase + string.digits  # Büyük harfler ve rakamlar
    kupon = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return kupon