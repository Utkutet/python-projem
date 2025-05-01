import time

from ortakfonksiyon import MARKET_KAYIT_DOSYASI, konsolu_temizle


def market_kayit():
    print("\n--- Kayıt Olma İşlemi ---")
    # Eğer dosya yoksa oluştur
    open(MARKET_KAYIT_DOSYASI, "a").close()
    
    while True:
        ad = input("Kullanıcı Adınızı Giriniz: ").strip()
        if ad == "":
            print("Kullanıcı adı boş bırakılamaz. Lütfen tekrar deneyin.")
            continue
        
        try:
            sifre = int(input("Şifrenizi Giriniz (sadece sayılar): "))
        except ValueError:
            print("Hatalı giriş! Şifre sadece sayılardan oluşmalıdır. Lütfen tekrar deneyin.")
            continue

        with open(MARKET_KAYIT_DOSYASI, "a") as dosya:
            dosya.write(f"{ad},{sifre}\n")
        print("Kayıt başarılı! Ana menüye yönlendiriliyorsunuz...")
        time.sleep(2)
        konsolu_temizle()
        break