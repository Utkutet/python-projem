from Banka.banka_giris_sayfasi import banka_giris_sayfasi
from ortakfonksiyon import konsolu_temizle
from Market.market_anamenü import market_anamenü

def anamenu():
    konsolu_temizle()
    while True:
        print("--- Ana Sayfa ---")
        print("1-) Market")
        print("2-) Banka")
        print("3-) Çıkış Yap")

        secim = input("Seçim Yapınız: ")

        if secim == "1":
            konsolu_temizle()
            market_anamenü()
        elif secim == "2":
            konsolu_temizle()
            banka_giris_sayfasi()
        elif secim == "3":
            exit()
        else:
            print("Geçersiz Seçim. Lütfen Tekrar Deneyin")

if __name__ == "__main__":
 anamenu()