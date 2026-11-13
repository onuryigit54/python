# Listeyi Döngü Yardımıyla Ekrana Basma
fiyatlar = [120, 250, 480, 90]
toplam = 0
print("=== Sepetteki Ürünlerin Fiyat Listesi ===")
for fiyat in fiyatlar:
    print(f"Ürün Tutarı: {fiyat:.2f} TL")
    toplam += fiyat # Her turda gelen fiyat toplam değişkenine eklenir.

print(f"Toplam Sepet Tutarı: {toplam:.2f} TL")