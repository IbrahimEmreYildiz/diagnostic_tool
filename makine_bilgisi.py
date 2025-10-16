# Makine Hakkında Bilgi Kodları

import socket

def makine_bilgisi_al():
    # Pc'nin adını alma yeri
    makine_adi = socket.gethostname()
    print("\nMakine adı:", makine_adi)

    # Makineden IP adresini alma yeri
    ip_adresi = socket.gethostbyname(makine_adi)
    print("IP Adresi:",  ip_adresi)

    # Bilgisayarın ağ üzerindeki gerçek ip adresini bulma yeri, yani diğer aynı ağa bağlı cihazların bizi tanıyacağı adres
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# Burada bir gönderme kanalı açtım. Parantezin içi ise ipv4 ve UDP kullanacağım anlamına gelir.
    try:
        s.connect(("8.8.8.8", 80))   # googlenin herkese açık adresine bağlanmayı deniyorum ki ağdaki ip adresimizi görelim. udp olduğu için gerçek bağlantı yok hata vermez o yüzden.
        yerel_ip = s.getsockname()  # yerel ip adresi ve port numarasını yazma fonksiyonu
    except Exception:
        local_ip = "Bağlantı hatası"
    finally:
        s.close()

    print("Yerel IP (aktif ağ) ve Port Numarası:", yerel_ip)

# Program direkt çalıştırıldığında fonksiyon çalışsın
if __name__ == "__main__":
    makine_bilgisi_al()
