# Siber Güvenlik Katmanı: İki Aşamalı Yetkilendirme Protokolü
sistem_parolasi = "Fatih1453"
dogrulama_kodu = 5532
girilen_parola = input("Sistem parolasını giriniz: ")
if girilen_parola == sistem_parolasi:
    print("1. Aşama Başarılı: Parola Doğrulandı.")
 
  # İç içe geçmiş ikinci kontrol katmanı (Girinti seviyesi 8 boşluğa çıktı.)
    girilen_kod = int(input("Telefonunuza gelen 4 haneli doğrulama kodunu giriniz: "))
   
    if girilen_kod == dogrulama_kodu:
        print("2. Aşama Başarılı: Kimlik Doğrulandı. Giriş Yapıldı.")
    else:
        print(" Doğrulama kodu hatalı. 2. Aşama Kod Hatası! Erişim Engellendi.")
else:
    print("Erişim Engellendi: Hatalı Sistem Parolası!")