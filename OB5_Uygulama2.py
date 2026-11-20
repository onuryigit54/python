# Kod-Asistan Profil Sözlüğü
# Kullanıcı tercihlerini (ad, dil, tema) iç içe sözlük yapısında saklar.

# b) Ana sözlük
kullanici_profili = {}

# c) İç içe (alt) sözlük tanımı
kullanici_profili["Kullanici_1"] = {
    "ad": "Kullanici_1",
    "dil": "Türkçe",
    "tema": "Açık",
}

print("Başlangıç profili:", kullanici_profili["Kullanici_1"])

# ç) Çalışma zamanında tema tercihini atama operatörüyle güncelleme
kullanici_profili["Kullanici_1"]["tema"] = "Koyu"
print("Güncellenmiş tema:", kullanici_profili["Kullanici_1"]["tema"])

# d) Var olmayabilecek "bildirim_sesi" anahtarını .get() ile güvenli sorgulama
bildirim_sesi = kullanici_profili["Kullanici_1"].get("bildirim_sesi")
print("bildirim_sesi ayarı:", bildirim_sesi)

# İsteğe bağlı: varsayılan değer ile güvenli erişim
print("bildirim_sesi (varsayılanlı):",
      kullanici_profili["Kullanici_1"].get("bildirim_sesi", "Ayar bulunamadı"))