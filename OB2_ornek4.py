# Senaryo A: Parantez Kullanılmayan Hatalı Durum (Mantık Hatası)
kilo = 70.0
boy = 1.75

# Python, aynı öncelikteki çarpma ve bölme işlemlerini soldan sağa değerlendirir. Önce kiloyu boya böler (70/1.75=40), sonra boyla çarpar (40*1.75=70).
hatali_vki = kilo / boy * boy
print("Hatalı Hesaplama:", hatali_vki) 
# Terminal Çıktısı: 70.0 (Mantıksız Sonuç)

# Senaryo B: Parantez ile İşlem Önceliğinin Yönetilmesi (Güvenli Çözüm)
# Parantez içi en yüksek önceliğe sahip olduğundan önce boy karesi (boy*boy) hesaplanır, sonra bölme yapılır.
dogru_vki = kilo / (boy * boy)
print(f"Doğru Hesaplama: {dogru_vki:.2f}")
# Terminal Çıktısı: 22.85 (Doğru Sonuç) 