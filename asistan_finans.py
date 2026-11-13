# KOD-ASİSTAN PROJESİ v1.2 - YARDIMCI FİNANSAL MODÜL
# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / Sadece Matematiksel Fonksiyon Hücrelerini Barındırır.
def net_tutar_hesapla(sepet_tutari, indirim_orani):
    """Gelen verileri işleyip net tutarı döndüren modül fonksiyonu"""
    indirim_miktari = sepet_tutari * (indirim_orani / 100)
    return sepet_tutari - indirim_miktari