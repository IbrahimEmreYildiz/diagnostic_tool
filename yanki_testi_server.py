# Yankı sunucusu

import socket

def yanki_sunucu():
    sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP soketi oluşturdum

    # Sunucu adresi ve portu
    host = "localhost"   # Bilgisayar
    port = 5000          # Yaygın olarak kullanılan port numarası

    # Soketi belirtilen IP ve porta bağla
    sunucu.bind((host, port))
    print(f"Sunucu başlatıldı ({host}:{port}), bağlantı bekleniyor...")

    # En fazla 1 tane bağlantı gelebilir şekilde ayarladım.
    sunucu.listen(1)

    # Bir bağlantı gelene kadar bekle
    baglanti, adres = sunucu.accept()
    print("Bağlantı kuruldu:", adres)

    # İstemciden gelen veriyi al
    veri_baytı = baglanti.recv(1024)  # 0 bayt veri gelirse hiç veri yollanmadı demek.
    if not veri_baytı:  # Kısaca veri alıp almadığımın kontrolü diyebiliriz.
        print("İstemci veri göndermeden bağlantıyı kapattı.")
        baglanti.close()
        sunucu.close()
        return

    # Gelen veriyi string'e çevir
    veri = veri_baytı.decode()  # decode() bayt olarak gelen veriyi string yapar.
    print("Gelen mesaj:", veri)

    # Aynı mesajı geri gönderdim. Yani yankı yaptım.
    baglanti.send(veri.encode())  # Veriyi göndermek için bayt türüne geri çevirir.
    print(" Mesaj yankılandı, istemciye gönderildi.")

    # Bağlantıyı kapat
    baglanti.close()
    sunucu.close()
    print("Sunucu kapatıldı.")

# Dosya doğrudan çalıştırıldığında
if __name__ == "__main__":
    yanki_sunucu()
