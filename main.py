# CEN322 Network Diagnostic and Tool Package

# Modülleri import ettim ekstra olarak threading, time modülünü ekledim
# çünkü yankı testinde ve sohbet modülünde iki ayrı terminal kullandım ve bunların beraber çalışmasını sağladım.
import threading, time
import makine_bilgisi
import yanki_testi_client
import yanki_testi_server
import zaman_alma
import sohbet_istemci
import sohbet_sunucu
import hata_yonetimi_ve_ayarlar

def main():
    while True: #Burası işlem bitince sürekli menüye dönmeyi sağlıyor.
        print("\n Network Diagnostic and Tool Package ")
        print("1. Makine Bilgisi")
        print("2. Yankı Testi (Echo Test)")
        print("3. Zaman Senkronizasyonu (SNTP)")
        print("4. Sohbet Modülü (Chat)")
        print("5. Hata Yönetimi ve Socket Ayarları")
        print("0. Çıkış")

        secim = input("\nSeçiminizi girin: ")

        # Makine Bilgisi
        if secim == "1":
            makine_bilgisi.makine_bilgisi_al()


        # Yankı Testi
        elif secim == "2":
            print("\n[Yankı Testi] Sunucu -> İstemci")
            threading.Thread(target=yanki_testi_server.yanki_sunucu, daemon=True).start()
            time.sleep(1)  # sunucunun bind/listen yapması için minicik gecikme
            yanki_testi_client.yanki_istemci()



        # Zaman Senkronizasyonu
        elif secim == "3":
            zaman_alma.zaman_al()

        # Sohbet Modülü
        elif secim == "4":
            print("\n[Sohbet] Sunucu -> İstemci")
            threading.Thread(target=sohbet_sunucu.sohbet_sunucu, daemon=True).start()
            time.sleep(0.3)
            sohbet_istemci.sohbet_istemci()

        # Hata Yönetimi ve Socket Ayarları
        elif secim == "5":
            hata_yonetimi_ve_ayarlar.hata_ve_ayar_testi()

        # Çıkış
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
