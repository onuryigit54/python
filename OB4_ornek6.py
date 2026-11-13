# =========================================================================
# PROJE ADI: KOD-ASİSTAN (Sürüm: v0.5 - Akıllı Maliyet Yönetimi)
# ÖRNEK: BULUT DEPOLAMA FATURA MODÜLÜ (VARSAYILAN PARAMETRE)
# =========================================================================
def fatura_kes(tutar, indirim_orani=10):
    """
    Bulut depolama ücretini hesaplar.
    indirim_orani parametresi boş bırakılırsa varsayılan olarak 10 kabul edilir.
    """
    # İndirimli net tutarın matematiksel olarak hesaplanması
    net_tutar = tutar - (tutar * indirim_orani / 100)
    return net_tutar
# --- FONKSİYONUN ANA AKIŞ İÇERİSİNDE TEST EDİLMESİ 
print("---KOD-ASİSTAN BULUT MALİYET RAPORU---")
# 1.SENARYO:Kurumsal / Kıdemli Kullanıcı(Özel İndirim Oranı Gönderildi)
# İkinci argüman olarak 20 gönderildiği için varsayılan değer (10) ezilir.
kurumsal_fatura=fatura_kes(1000,20)
print(f"1. Senaryo (Yönetici İndirimi %20) -> Ödenecek Tutar:{kurumsal_fatura:.2f} TL")
# 2.SENARYO:Standart /Misafir Kullanıcı (Tek Argüman Gönderildi)
# İkinci argüman boş bırakıldığı için fonksiyon otomatik olarak indirim_orani = 10 alır.
standart_fatura = fatura_kes(1000)
print(f"2. Senaryo (Standart İndirim %10) -> Ödenecek Tutar:{standart_fatura:.2f}TL")