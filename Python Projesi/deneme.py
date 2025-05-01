import time

def yüklemeekranı(sure=4, adim_sayisi=20):
    print("Lütfen Bekleyiniz...")
    for i in range(adim_sayisi + 1):
        yuzde = int((i / adim_sayisi) * 100)
        cubuk = "=" * i + "-" * (adim_sayisi - i)
        print(f"\r[{cubuk}] {yuzde}%", end="", flush=True)
        time.sleep(sure / adim_sayisi)  # Her adım için bekleme süresi

def banka_giris_mesajı():
    lines = [
        "+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+",
        "|  C  |   |  I  |   |  F  |   |  T  |   |  L  |   |  I  |   |  K  |",
        "+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+",
        "",
        "+-----+   +-----+   +-----+   +-----+   +-----+",
        "|  B  |   |  A  |   |  N  |   |  K  |   |  A  |",
        "+-----+   +-----+   +-----+   +-----+   +-----+",
        "",
        "+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+",
        "|  H  |   |  O  |   |  S  |   |  G  |   |  E  |   |  L  |   |  D  |   |  I  |   |  N  |   |  I  |   |  Z  |",
        "+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+",
    ]

    for line in lines:
        print(line)
        time.sleep(0.25)