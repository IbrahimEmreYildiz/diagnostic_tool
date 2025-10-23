# SNTP (Simple Network Time Protocol) Modülü

import ntplib # İnternetten tarih ve saat çekmeye yarayan kütüphane
from time import ctime # ctime, time kütüphanesinde bir fonksiyon ve tarihi bizim okuyabileceğimiz şekle getiriyor.

def zaman_al(): # İşlemin yapıldığı tarihi ve saati yazdırır.
    try:                                          # Hata olursa sistem çökmesin diye bu yapıyı kullandım.
        istemci = ntplib.NTPClient()              # NTP istemcisi oluştur. Saat isteği göndermek için oluşturdum.
        yanit = istemci.request('pool.ntp.org')   # Zaman sunucusuna tarih saat için istek attım. pool.ntp.org saati aldığım yer.
        print("Sunucudan alınan zaman:", ctime(yanit.tx_time))  # Zamanı okunabilir hale getirdim.
    except Exception as hata:
        print("Zaman alınamadı:", hata)

if __name__ == "__main__":
    zaman_al()
