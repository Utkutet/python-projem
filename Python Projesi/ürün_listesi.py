# Her bir kategori için ürünlerin tanımlandığı liste
yiyecekler = [
    {"isim": "Muz(Yerli)", "fiyat": 65},
    {"isim": "Limon", "fiyat": 36},
    {"isim": "Avokado", "fiyat": 40},
    {"isim": "Karpuz", "fiyat": 50},
    {"isim": "Portakal", "fiyat": 40}

]

içecekler = [
    {"isim": "Erikli Doğal Kaynak Suyu 6x1 L", "fiyat": 115},
    {"isim": "Kurukahveci Mehmet Efendi Türk Kahvesi 100 G", "fiyat": 65},
    {"isim": "Sütaş Pratik Şişe Ayran 1 L", "fiyat": 30},
    {"isim": "Kızılay Afyonkarahisar Doğal Maden Suyu 6x200 Ml", "fiyat": 35},
    {"isim": "Monster Ultra Şekersiz Enerji İçeceği Kutu 500 ML", "fiyat": 50}
]

eşyalar = [
    {"isim": "Koltuk", "fiyat": 1500},
    {"isim": "Uzay istasyonu", "fiyat": 250000},
    {"isim": "Monitör", "fiyat": 10000}
]

# Ürünlerin listelerini döndüren fonksiyonlar
def kategori_getir(kategori):
    if kategori == "yiyecekler":
        return yiyecekler
    elif kategori == "içecekler":
        return içecekler
    elif kategori == "eşyalar":
        return eşyalar
    else:
        return []