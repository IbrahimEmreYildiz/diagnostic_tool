# chat_server.py
# Basit Sohbet Sunucusu (TCP)
# Amaç: İstemciden mesaj al, ekrana yaz; senin yazdığını istemciye gönder.
# Not: 'exit' yazan taraf sohbeti bitirir.

import socket

def sohbet_sunucu():
    host = "localhost"
    port = 6000          # Client ile aynı olsa kâfi


    sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP


    sunucu.bind((host, port))
    sunucu.listen(1)
    print(f"Sunucu hazır ({host}:{port}), bağlantı bekleniyor...")

    baglanti, adres = sunucu.accept()
    print("Bağlantı kuruldu:", adres)

    try:
        while True:
            veri = baglanti.recv(1024)
            if not veri:
                print("İstemci bağlantıyı kapattı.")
                break

            mesaj = veri.decode()
            print(f"[İstemci]: {mesaj}")

            # exit yazarlarsa sohbet biter.
            if mesaj.strip().lower() == "exit":
                print("İstemci sohbeti sonlandırdı.")
                break

            # 5) istemciye cevap verme kısmı
            cevap = input("[Sen]: ")
            baglanti.send(cevap.encode())

            # exit denirse bitir
            if cevap.strip().lower() == "exit": #strip fonksiyonu karakterler arası boşluğu yoksayar. lower() ise tüm harfleri küçültür.
                print("Sohbet sonlandırıldı.")
                break
    finally:
        baglanti.close()
        sunucu.close()
        print("Sunucu kapatıldı.")

if __name__ == "__main__":
    sohbet_sunucu()
