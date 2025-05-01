from ortakfonksiyon import MARKET_KAYIT_DOSYASI, konsolu_temizle

giris_yapan_kullanici = None #Global Değişken

def market_giris():
    global giris_yapan_kullanici
    print("--- Giriş Yap ---")
    
    try:
        # Kullanıcı adı ve şifre girişi
        ad = input("Kullanıcı Adınızı Giriniz: ").strip()
        sifre = input("Şifrenizi Giriniz: ").strip()
        
        # Dosyadan kullanıcı bilgilerini okuma
        with open("market_kullanicilar.txt", "r") as dosya:
            kullanicilar = dosya.readlines()
        
        # Kullanıcı adı ve şifre kontrolü
        for kullanici in kullanicilar:
            kayitli_ad, kayitli_sifre = kullanici.strip().split(",")
            if ad == kayitli_ad and sifre == kayitli_sifre:
                giris_yapan_kullanici = kayitli_ad #kayıtlı adı global değişkene ekliyoruz
                #temizle ekle
                konsolu_temizle()
                print(f"Hoşgeldiniz, {ad}!")
                from Market.market_islemleri import market_islemleri
                market_islemleri()
                return True
        
        # Hatalı giriş
        print("Hatalı kullanıcı adı veya şifre. Lütfen tekrar deneyin.")
        return False
    
    except FileNotFoundError:
        print("Kullanıcı veritabanı bulunamadı. Lütfen önce kayıt olun.")
        return False
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return False