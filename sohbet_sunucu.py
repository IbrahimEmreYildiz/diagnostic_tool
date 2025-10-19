# Basit Sohbet Sunucusu (TCP)

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


    # log komutuyla sohbetin geçmişini kaydettim.
    try:
       # open ile dosya oluşturup (chat.log adında), append yani 'a' dosya varsa silmez üstüne ekler utf-8 ise Türkçe karakterleri sorunsuz yazar.
        with open("chat.log", "a", encoding="utf-8") as log: # with kullanınca dosyayı kapatmama gerek kalmadı. as log ise dosyaya log adını ver demek.
            log.write(f"\n Yeni Sohbet Başladı ({adres}) \n")

            while True:
                veri = baglanti.recv(1024)
                if not veri:
                    print("İstemci bağlantıyı kapattı.")
                    log.write("İstemci bağlantıyı kapattı.\n")
                    break

                mesaj = veri.decode()
                print(f"[İstemci]: {mesaj}")
                log.write(f"[İstemci]: {mesaj}\n")

                # exit yazarlarsa sohbet biter.
                if mesaj.strip().lower() == "exit":
                    print("İstemci sohbeti sonlandırdı.")
                    log.write("İstemci sohbeti sonlandırdı.\n")
                    break

                # 5) istemciye cevap verme kısmı
                cevap = input("[Sen]: ")
                baglanti.send(cevap.encode())
                log.write(f"[Sunucu]: {cevap}\n")

                # exit denirse bitir
                if cevap.strip().lower() == "exit": #strip fonksiyonu karakterler arası boşluğu yoksayar. lower() ise tüm harfleri küçültür.
                    print("Sohbet sonlandırıldı.")
                    log.write("Sunucu sohbeti sonlandırdı.\n")
                    break

            log.write("Sohbet Bitti \n")
    finally:
        baglanti.close()
        sunucu.close()
        print("Sunucu kapatıldı.")

if __name__ == "__main__":
    sohbet_sunucu()
