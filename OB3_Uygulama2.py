
# AKILLI GÜVENLİK KAPISI

# Kullanıcıdan rol bilgisini al
rol = input("Rolünüzü giriniz (Yönetici/Personel): ")

# Rol bilgisini küçük harfe dönüştür
rol = rol.lower().strip()

# Rol kontrolü
if rol == "yonetici":
    print("Erişim izni verildi. Hoş Geldiniz Sayın Yönetici.")

elif rol == "personel":

    # Personelin güvenlik derecesini al
    guvenlik = int(input("Güvenlik derecenizi giriniz: "))

    # İç içe if kontrolü
    if guvenlik >= 3:
        print("Erişim izni verildi. Laboratuvar alanına geçebilirsiniz.")
    else:
        print("Erişim engellendi. Yetersiz güvenlik derecesi!")

else:
    print("Hatalı rol tanımlaması! Güvenlik protokolü devreye girdi.")
