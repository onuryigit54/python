print("=== DİJİTAL ESER KATALOĞU YÜKLENİYOR ===\n")
# 1. AŞAMA: İç İçe Sözlük (Nested Dictionary) Mimarisinin Kurulması
eser_katalogu = {
    "Dîvân-ı Hikmet": {
        "yazar": "Hoca Ahmed Yesevî"
    },
    "Mesnevî": {
        "yazar": "Mevlânâ"
    },
    "Risaletü’n Nushiyye": {
        "yazar": "Yunus Emre"
    }
}
# 2. AŞAMA: Zincirleme Veri Erişimi ve Dinamik Ekleme
ikinci_eser_yazari = eser_katalogu["Mesnevî"]["yazar"]
print(f"Mesnevî adlı eserin yazarı: {ikinci_eser_yazari}")
print("\n[BİLGİ] 'Dîvân-ı Hikmet' eseri için 'tür' bilgisi ekleniyor...")
eser_katalogu["Dîvân-ı Hikmet"]["tür"] = "Tasavvuf"
print(f"Güncel Dîvân-ı Hikmet Kaydı: {eser_katalogu['Dîvân-ı Hikmet']}")
# 3. AŞAMA: .get() Metodu ile Güvenli Veri Sorgulama (KeyError Önleme)
print("\n[SORGULAMA] Risaletü’n Nushiyye eseri için basım yılı aranıyor...")
basim_bilgisi = eser_katalogu["Risaletü’n Nushiyye"].get("basim_yili", "Basım yılı bilgisi bulunamadı.")
print(f"Basım Yılı: {basim_bilgisi}")
print("==================================================")