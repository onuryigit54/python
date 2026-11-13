sepet_tutari = float(input("Lütfen mevcut sepet tutarını giriniz (TL): "))
kullanici_yasi = int(input("Lütfen yaşınızı giriniz: "))
# Kampanya parametresinin mantıksal (boolean) olarak tanımlanması
kupon_kod_aktif_mi = True
# BİRLEŞİK OPERATÖR KULLANIMI VE İŞLEM ÖNCELİĞİ ALANI
# Önce parantez içi (or) hesaplanır, çıkan sonuç kupon aktifliği ile (and) bağlanır.
indirim_onaylandi_mi = kupon_kod_aktif_mi and (kullanici_yasi >= 18 or sepet_tutari >
500)
print("\n--- Mantıksal Analiz Sonucu ---")
print(f"Kupon Durumu: {kupon_kod_aktif_mi}")
print(f"Birleşik Şart Sağlandı mı?: {indirim_onaylandi_mi}")
print("--------------------------------")
# Karar mekanizmasının işletilmesi
if indirim_onaylandi_mi:
    indirim_miktari = sepet_tutari * 0.10
    odenecek_tutar = sepet_tutari - indirim_miktari
    print(f"Tebrikler! Kampanya şartlarını sağladınız.")
    print(f"Uygulanan İndirim: {indirim_miktari:.2f} TL")
    print(f"Net Ödenecek Tutar: {odenecek_tutar:.2f} TL")
else:
    print(f"Maalesef kampanya şartları sağlanamadı.")
    print(f"Net Ödenecek Tutar: {sepet_tutari:.2f} TL") 