# REFACTORING SONRASI KOD-ASİSTAN v1.3
# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / DRY Prensibi / Fonksiyonel Optimizasyon
print("=== KOD-ASİSTAN: REFACTORING KALİTE DENETİM MOTORU ===\n")
def indirimli_sistem_kontrolu(kullanici_tipi, sepet_tutari):
    """Kullanıcı tipini ve sepet tutarını alarak ödenecek tutarı döndürür."""
    print(f"[SİSTEM] {kullanici_tipi} erişim katmanı doğrulanıyor...")
    if sepet_tutari > 500:
        net_tutar = sepet_tutari * 0.90
        print(f"{kullanici_tipi} için indirim uygulandı. Ödenecek: {net_tutar:.2f} TL")
    else:
        net_tutar = sepet_tutari
        print(f"{kullanici_tipi} için indirim yok. Ödenecek: {sepet_tutari:.2f} TL")
        return net_tutar
# FONKSİYONUN FARKLI ARGÜMANLARLA TEKRAR KULLANILMASI (DRY UYUMU)
indirimli_sistem_kontrolu("Yönetici", 600)
indirimli_sistem_kontrolu("Öğretmen", 450)
indirimli_sistem_kontrolu("Öğrenci", 800)