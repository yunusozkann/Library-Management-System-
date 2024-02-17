class Kutuphane:
    def __init__(self):
        self.dosya = open("kitaplar.txt", "a+")
        self.dosya.seek(0)  # Dosyanın başına gidin

    def __del__(self):
        self.dosya.close()

    def kitapları_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        if not kitaplar:
            print("Hiç kitap bulunamadı.")
        else:
            print("Kitap Listesi:")
            for kitap in kitaplar:
                kitap_bilgisi = kitap.strip().split(',')
                print(f"Başlık: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        baslik = input("Kitap başlığını girin: ")
        yazar = input("Kitap yazarını girin: ")
        yayin_tarihi = input("Yayın tarihini girin: ")
        sayfa_sayisi = input("Sayfa sayısını girin: ")

        kitap_bilgisi = f"{baslik},{yazar},{yayin_tarihi},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap başarıyla eklendi.")

    def kitap_sil(self):
        baslik = input("Silmek istediğiniz kitabın başlığını girin: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        bulundu = False
        güncellenmiş_kitaplar = []
        for kitap in kitaplar:
            if baslik.lower() not in kitap.lower():
                güncellenmiş_kitaplar.append(kitap)
            else:
                bulundu = True
        if not bulundu:
            print("Kitap bulunamadı.")
        else:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(güncellenmiş_kitaplar)
            print("Kitap başarıyla silindi.")


kutuphane = Kutuphane()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("4) Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        kutuphane.kitapları_listele()
    elif secim == '2':
        kutuphane.kitap_ekle()
    elif secim == '3':
        kutuphane.kitap_sil()
    elif secim == '4':
        break
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek girin.")
