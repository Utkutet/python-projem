from ortakfonksiyon import konsolu_temizle


def market_anamenü():
    while True:
        try:
            print("--- Market Ana Menü ---")
            print("1. Kayıt Ol")
            print("2. Giriş Yap")
            print("3. Çıkış")
            
            secim = int(input("Hangi işlemi yapmak istiyorsunuz (1-3): "))

            if secim == 1:
                from Market.market_kayit import market_kayit
                market_kayit()
            elif secim == 2:
                konsolu_temizle()
                from Market.market_giris import market_giris
                market_giris()
            elif secim == 3:
                print("Çıkış yapılıyor...")
                konsolu_temizle()
                break
            else:
                print("Geçersiz seçim! Lütfen 1-3 arasında bir değer giriniz.")
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")