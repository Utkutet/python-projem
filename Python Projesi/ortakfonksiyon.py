import os
import random

KAYIT_DOSYASI = "kullanıcılar.txt"
MARKET_KAYIT_DOSYASI ="market_kullanicilar.txt"
INDIRIM_KUPONU = "indirim_kuponu.txt"
BILDIRIMLER = "bildirimler.txt"
SATIN_ALIMLAR = "satın_alınan.txt"

def kart_numarasi_olustur():
    return "".join([str(random.randint(0,9)) for _ in range(16)])

def ccv_olustur():
    return "".join([str(random.randint(1,9)) for _ in range(3)])

def tarih_olustur():
    ilk_hane = random.randint(1, 12)

    # Sonrasında '30' sabit olarak eklenir
    return f"{str(ilk_hane).zfill(2)}/30"


def konsolu_temizle():
    os.system('cls' if os.name == 'nt' else ' clear')