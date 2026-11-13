# Standart dışı girdi senaryosu
girdi = "EvEt"
# Yöntem A: Metot kullanılmayan durum (Mantıksal Hata Riski)
if girdi == "evet":
    print("İşlem onaylandı.") # Bu blok çalışmaz, çünkü "EvEt" == "evet" sonucu False’tur.
# Yöntem B: Kararlı Dönüşüm Yapılmış Durum (Önerilen Standart)
temiz_girdi = girdi.lower() # "EvEt" verisi tamamen küçük harfe dönüştürülerek "evet" olur.
if temiz_girdi == "evet":
    print("İşlem başarıyla onaylandı.") # Bu blok kararlı bir şekilde çalışır.