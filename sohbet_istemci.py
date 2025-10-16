# chat_client.py
# Basit Sohbet İstemcisi (TCP)
# Amaç: Sunucuya bağlan, mesaj gönder ve gelen cevabı al.
# Not: 'exit' yazan taraf sohbeti bitirir.

import socket

def sohbet_istemci():
    host = "localhost"
    port = 6000

    istemci = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    istemci.connect((host, port))
    print(f"Sunucuya bağlanıldı ({host}:{port})")

    try:
        while True:
            # 3) Mesaj yaz ve gönder
            mesaj = input("[Sen]: ")
            istemci.send(mesaj.encode())

            # Eğer 'exit' yazılırsa sohbeti bitir
            if mesaj.strip().lower() == "exit":
                print("Sohbet sonlandırıldı.")
                break

            # 4) Sunucudan cevap al
            cevap = istemci.recv(1024).decode()
            print(f"[Sunucu]: {cevap}")

            # Sunucu 'exit' dediyse sohbet biter
            if cevap.strip().lower() == "exit":
                print("Sunucu sohbeti kapattı.")
                break
    finally:
        istemci.close()
        print("Bağlantı kapatıldı.")

if __name__ == "__main__":
    sohbet_istemci()
