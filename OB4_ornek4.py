def inc_to_cm(inc_degeri):
    """
    Aldığı inç değerini 2.54 sabiti ile çarparak santimetreye dönüştürür.
    Elde edilen sonucu ekrana basmaz, çağrıldığı yere döndürür (return).
    """
    # 1 inç = 2.54 cm’dir.
    cm_sonuc = inc_degeri * 2.54
    return cm_sonuc
# --- FONKSİYONUN ANA AKIŞ İÇERİSİNDE ÇAĞRILMASI (MAIN FLOW) 
# --print("---KOD-ASİSTAN DONANIM ÖLÇÜM DÖNÜŞTÜRÜCÜ---")
#Kullanıcıdan dönüştürülecek inç verisinin dinamik olarak alınması.
tasarim_inci=float(input("Lütfen dönüştürülecek ölçüyü giriniz (İnç):"))
#Fonksiyon çağrılıyor(call) ve return edilen veri ‘hesaplanan_cm’ değişkenine aktarılıyor.
hesaplanan_cm=inc_to_cm(tasarim_inci)
# Ana akışa aktarılan veri, artık sistemin istenen yerinde özgürce kullanılabilir.
print(f"Dönüşüm Tamamlandı: {tasarim_inci} inç ={hesaplanan_cm:.2f}cm’dir.")
#Veri aktarımının kanıtı: Döndürülen santimetre değeri başka bir koşulun denetlenmesinde kullanılır.
if hesaplanan_cm > 50:
    print("Sistem Uyarısı: Bu donanım boyutu standart asistan paneli için büyüktür.")