# =========================================================================
# KOD-ASİSTAN PROJESİ - KALICI HAFIZA (LOG) VE DOSYA YÖNETİMİ
# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / I/O İşlemleri ve Exception Handling (Hata Yönetimi)
# =========================================================================
print("=== KOD-ASİSTAN HAFIZA VE LOG YÖNETİMİ ===\n")
# 1. AŞAMA: Dosyadan Veri Okuma ('r' - Read Modu) ve İstisna Yönetimi
print("\n--- GEÇMİŞ İŞLEM KAYITLARI (HAFIZA DÖKÜMÜ) ---")
try:
    # Dosya okuma modunda açılır. Program çökme riskine karşı ‘try’ (dene) blokundadır.
    with open("asistan_hafiza.txt", "r", encoding="utf-8") as dosya:
        gecmis_veriler = dosya.read()
        print(gecmis_veriler)
except FileNotFoundError  as e:
    # Eğer asistan_hafiza.txt bilgisayarda bulunamazsa program çökmez, bu bloka düşer.
       print(f"[SİSTEM UYARISI] Hafıza dosyası bulunamadı! Detay: {e}")

# 2. AŞAMA: Dosyaya Veri Ekleme (‘a’ - Append Modu)
kullanici_komutu = input("Asistana kaydetmek istediğiniz notu/komutu giriniz: ")
# ‘a’ modu: Dosya yoksa oluşturur, varsa içeriğini silmeden en sona (kuyruğa) ekler.
with open("asistan_hafiza.txt", "a", encoding="utf-8") as dosya:
    dosya.write(f"-> Sistem Kaydı: {kullanici_komutu}\n")
print("\n[BİLGİ] Veriniz sabit diske (asistan_hafiza.txt) kalıcı olarak kaydedildi.")