# ==============================================================
# YAPAY ZEKÂ TARAFINDAN ÜRETİLEN KARARSIZ KOD TASLAĞI
# DİKKAT: Bu kod mantıksal ve yapısal hatalar barındırmaktadır!
# ==============================================================

sepet_listesi = [100.0, 250.0, 75.0]
print("--- Yapay Zekâ Sepet Yönetim Sistemi ---")

while True:
    girdi = input("Ürün fiyatı giriniz veya çıkmak için 'ÇIKIŞ' yazınız: ")

    if girdi.upper() == "ÇIKIŞ":
        print("Hesaplama yapılıyor...")
        break

    else:
        try:
            fiyat = float(girdi)

            if fiyat > 0:
                sepet_listesi.append(fiyat)
                print(f"Ürün eklendi. Sepetteki Ürün Sayısı: {len(sepet_listesi)}")
            else:
                print("Fiyat sıfırdan büyük olmalıdır.")

        except ValueError:
            print("Lütfen geçerli bir sayısal fiyat giriniz.")

sayac = 0

while sayac < 3:
    print(f"Doğrulanıyor... İşlem Sırası: {sayac + 1}")
    sayac += 1

son_indeks = len(sepet_listesi) - 1

print(f"En son eklenen ürünün fiyatı: {sepet_listesi[son_indeks]} TL")
