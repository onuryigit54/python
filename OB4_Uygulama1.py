# ======================================================================
# PROJE ADI: KOD-ASİSTAN (Sürüm: v0.4 - Modüler Dönüşüm)
# ETKİNLİK: SELAMLAMA VE HESAPLAMA MODÜLÜ (PARAMETRE VE RETURN)
# ======================================================================
# 1. AŞAMA: MODÜLER FONKSİYONLARIN TANIMLANMASI
def karsilama_modulu(ad, rol):
    """
    Kullanıcının ad ve rol bilgilerini parametre olarak alıp,
    kişiselleştirilmiş selamlama metnini return ile fırlatır.
    """
    # f-string ile bellekte metin biçimlendirme (Ekrana basılmaz, döndürülür.)
    selamlama_metni = (f"Hoş geldiniz {ad}. Sistemdeki rolünüz: [{rol}]. Kod-Asistan sizi selamlıyor!")
    return selamlama_metni
def yas_hesapla(dogum_yili, mevcut_yil):
    """
    Doğum yılı ve mevcut yıl parametrelerini alarak yaklaşık yaş hesabı yapar ve elde
edilen tam sayı sonucu return eder.
    """
    # 4 boşluklu girinti kuralına uygun hesaplama bloku
    hesaplanan_yas = mevcut_yil - dogum_yili
    return hesaplanan_yas
# 2. AŞAMA: ANA AKIŞIN (MAIN FLOW) KURULMASI VE FONKSİYONLARIN ÇAĞRILMASI
# Kullanıcıdan dinamik veri alımı ve veri türü tuzaklarının engellenmesi
print("--- KOD-ASİSTAN KULLANICI GİRİŞ PANELİ ---")
giris_adi = input("Lütfen adınızı giriniz: ")
giris_rolu = input("Sistem rolünüzü giriniz (Yönetici/Misafir): ")
# Tür dönüşümü (Type casting) yapılarak input verisi int formatına dökülüyor.
dogum_tarihi = int(input("Lütfen doğum yılınızı giriniz (Örn: 2005): "))
guncel_yil = 2026  # Örnek sabit yıl. İstenirse datetime modülüyle dinamik alınabilir.
print("\n--- SİSTEM RAPORU VE ÇIKTILAR ---")
# karsilama_modulu fonksiyonunun çağrılması (call) ve sonucun yakalanması
asistan_mesaji = karsilama_modulu(ad=giris_adi, rol=giris_rolu)
print(asistan_mesaji)  # Return edilen veri burada ekrana yazdırılıyor.
# yas_hesapla fonksiyonunun çağrılması ve sonucun yakalanması
kullanici_yasi = yas_hesapla(dogum_yili=dogum_tarihi, mevcut_yil=guncel_yil)
print(f"Sistem tarafından hesaplanan güncel yaşınız: {kullanici_yasi}")