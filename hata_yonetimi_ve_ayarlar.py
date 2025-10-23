# Soket ayarları ve hataları gösterme

import socket

def hata_ve_ayar_testi(host="localhost", port=5000):
    print("Socket Ayarları ve Hata Yönetim Testi")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP soketi
    try:

        print("Bloklama modu :", s.getblocking())  # Bloklamadan kastım herhangi bir bağlantı kurulana kadar veya veri görene kadar bekle demek. Default mod olarak kullanılır.
        # Bloklama modu true değer olarak geçer.

        s.settimeout(3.0)
        print("Zaman Aşımı:", s.gettimeout(), "saniye") # Herhangi bir işlem gerçekleşmezse işlemi zaman aşımına uğratır. Buradan ayarlayabilirsin.


        mevcut_tampon_boyutu = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("Mevcut Tampon Boyutu:", mevcut_tampon_boyutu, "byte") # Tampon bölge yani veriyi gönderdiğimde geçici olarak burada depolanır recv() fonksiyonu çalışınca buradan alınır.

        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096) # Yeni tampon boyutum 4 kilobayt oldu örnek olarak, bu sayı değiştirilebilir.
        yeni_tampon_boyutu = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("Yeni Tampon Boyutu:", yeni_tampon_boyutu, "byte")

        # (Opsiyonel) bloklamasız moda geçmek için:
        # s.setblocking(False) bloklama true değer olduğu için false değerini verince otomatik olarak bloklamasız moda geçer.

        print(f" {host}:{port} adresine bağlanılmaya çalışılıyor.")
        s.connect((host, port))  # Sunucu yoksa 'bağlantı reddedildi' hatası gelebilir
        print("Bağlantı kuruldu!")

        # Gönderim tamponu boyutu
        mevcut_gonderim_tamponu = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        print("Mevcut Gönderim Tamponu:", mevcut_gonderim_tamponu, "byte")
        s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
        yeni_gonderim_tamponu = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        print("Yeni Gönderim Tamponu:", yeni_gonderim_tamponu, "byte")

        # Bloklama modu kapalı ve test etme yeri
        s.setblocking(False)
        print("Bloklama modu değiştirildi:", s.getblocking())
        try:
            s.send(b"Test veri") # Burada 'b' bayt dizisi anlamına geliyor. Çünkü soketler sadece bayt olarak veri alıp verir. Denemek için test verisi yolladım.
        except BlockingIOError:
            print("Non-blocking modda: Veri henüz gönderilemedi.")

    except socket.timeout:
        print("Hata: Bağlantı denemesi zaman aşımına uğradı.") # Koyduğum süre boyunca yanıt vs gelmediği anlamına geliyor.
    except ConnectionRefusedError: #Bağlantı reddedildi demek
        print("HATA: Bağlantı reddedildi (Sunucu kapalı olabilir. Kontrol edin.).") # Sunucu açık olmayabilir o yüzden alınabilir.
    except socket.gaierror: # DNS düzgün çalışmadı vs. demek yani IP 'ye dönüştürülemedi demek.
        print("Hata: Host çözümlenemedi (DNS/host hatası).") # Siteyi IP'ye dönüştüremeyince oluyor genelde
    except OSError as detay: # İşletim sistemi hatası demek.
        print("Hata: İşletim sistemi hatası:", detay) #Donanımsal hata olabilir internet kablosu wifi falan filan.
    finally:
        s.close()
        print(" Soket kapatıldı.")

if __name__ == "__main__":
    hata_ve_ayar_testi()
