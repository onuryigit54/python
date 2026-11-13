# kumbara_asistani.py

# b) Kullanıcıdan kumbaraya atılan TL miktarını ve güncel döviz kurunu talep etme
tl_miktari_giris = input("Kumbaraya atılan TL miktarını giriniz: ")
doviz_kuru_giris = input("Güncel döviz kurunu giriniz (Örn: 34.55): ")

# c) Metinsel (str) verileri matematiksel işlemler için ondalıklı sayıya (float) dönüştürme
tl_miktari = float(tl_miktari_giris)
doviz_kuru = float(doviz_kuru_giris)

# ç) Döviz karşılığını hesaplayan matematiksel formül
doviz_karsiligi = tl_miktari / doviz_kuru

# ç) Oluşan sonucu f-string mimarisiyle ekrana yazdırma (.2f ile virgülden sonra iki basamak gösterilir)
print(f"Kumbaraya eklenen {tl_miktari} TL tutarının döviz karşılığı: {doviz_karsiligi:.2f}$")
