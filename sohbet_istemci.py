# Basit Sohbet İstemcisi (TCP)

import socket

def sohbet_istemci():
    host = "localhost"
    port = 6000

    istemci = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    istemci.connect((host, port))
    print(f"Sunucuya bağlanıldı ({host}:{port})")

    try:

        with open("chat.log", "a", encoding="utf-8") as log: # chat.log adında append yani eklemeli ve Türkçe kelimelerin hata yaratmayacağı şekilde dosya oluştur.
            log.write(f"\n Yeni Sohbet Başladı (istemci) \n")

            while True:
                # 3) Mesaj yazıp ve gönderme yeri
                mesaj = input("[Sen]: ")
                istemci.send(mesaj.encode())
                log.write(f"[İstemci]: {mesaj}\n")

                # Eğer exit yazılırsa sohbeti bitir
                if mesaj.strip().lower() == "exit":
                    print("Sohbet sonlandırıldı.")
                    log.write("İstemci sohbeti sonlandırdı.\n")
                    break

                # 4) Sunucudan cevap al
                cevap = istemci.recv(1024).decode()
                print(f"[Sunucu]: {cevap}")
                log.write(f"[Sunucu]: {cevap}\n")

                # Sunucu 'exit' dediyse sohbeti bitir.
                if cevap.strip().lower() == "exit":
                    print("Sunucu sohbeti kapattı.")
                    log.write("Sunucu sohbeti kapattı.\n")
                    break

            log.write("Sohbet Bitti\n")
    finally:
        istemci.close()
        print("Bağlantı kapatıldı.")

if __name__ == "__main__":
    sohbet_istemci()
