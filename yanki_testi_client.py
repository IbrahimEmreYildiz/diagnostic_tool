#Yankı İstemcisi

import socket

def yanki_istemci():
    istemci = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP soketi oluştur

    # Sunucu adresi ve portu server ile aynı olmalı yoksa mesaj için aynı portta buluşup kontrol sağlayamaz.
    host = "localhost"
    port = 5000 # Test için yaygın olarak 5000. port kullanıldığı için bunu seçtim.

    # Sunucuyla bağlantı kur.
    istemci.connect((host, port))
    print("Sunucuyla bağlantı kuruldu.")

    # Kullanıcıdan mesaj al
    mesaj = input("Test mesajı yaz: ")

    # Mesajı sunucuya gönder
    istemci.send(mesaj.encode()) # Mesajı bayt türüne dönüştürür.

    # Sunucudan gelen cevabı al.
    cevap = istemci.recv(1024).decode()

    # Gelen mesaj ile giden mesajı karşılaştırır eğer aynıysa bağlantı başarılı demektir.
    if mesaj == cevap:
        print("Bağlantı başarılı, veri aynı!")
    else:
        print("Veri uyuşmuyor!")

    # Bağlantıyı kopart.
    istemci.close()
    print("İstemci kapatıldı.")

# Dosya doğrudan çalıştırıldığında
if __name__ == "__main__":
    yanki_istemci()
