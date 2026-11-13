# Kullanıcıdan dinamik ve kararlı veri girişinin alınması
kullanici_metni = input("Lütfen analiz edilecek metni giriniz: ")
print("\n=== GELİŞMİŞ KARAKTER ANALİZ RAPORU ===")
# for döngüsü ile girilen metnin her bir karakterinin taranması
for harf in kullanici_metni:
    # .upper() metodu ile taranan karakterin büyük harfe dönüştürülmesi
    buyuk_harf = harf.upper()
    # F-String teknolojisi ile daha zengin ve formatlı bir çıktı üretilmesi
    print(f"Tespit Edilen Karakter -> [ {buyuk_harf} ]")
print("=======================================")