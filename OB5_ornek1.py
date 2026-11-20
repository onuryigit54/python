print("--- DİJİTAL ENVANTER YÖNETİM SİSTEMİ ---")

# 1. Aşama: Sözlük oluşturma
stok_envanteri = {
    "Laptop": 45,
    "Telefon": 120,
    "Kulaklık": 300
}

# 2. Aşama: Anahtar kullanarak değere erişim
telefon_stogu = stok_envanteri["Telefon"]
print(f"Güncel Telefon Stoğu: {telefon_stogu} adet")

# 3. Aşama: Yeni veri ekleme
stok_envanteri["Tablet"] = 50
print("\n[BİLGİ] Tablet ürünü envantere eklendi.")

# 4. Aşama: Mevcut değeri değiştirme (Güncelleme)
stok_envanteri["Laptop"] = 40
print("[BİLGİ] Laptop stoğu 40 olarak güncellendi.")

# 5. Aşama: Sözlükten veri silme (del)
del stok_envanteri["Kulaklık"]
print("[BİLGİ] Kulaklık ürünü envanterden tamamen silindi.")

# 6. Aşama: Sözlük metotları ile içeriği görüntüleme (keys, values, items)
print("\n--- ENVANTER METOT ANALİZİ ---")
print("Anahtarlar (Kayıtlı Ürünler):", stok_envanteri.keys())
print("Değerler (Stok Miktarları):", stok_envanteri.values())
print("Çiftler (Tüm Kayıtlar):", stok_envanteri.items())

# 7. Aşama: for döngüsü kullanımı ile listeleme
print("\n--- GÜNCEL ENVANTER DURUMU (FOR DÖNGÜSÜ İLE) ---")
for urun, adet in stok_envanteri.items():
    print(f"-> {urun} : {adet} adet stokta mevcuttur.")