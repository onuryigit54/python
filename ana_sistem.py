import guvenlik_araclari as ga

yeni_parola = ga.parola_uret()
print(f"Üretilen geçici parola: {yeni_parola}")

# Sınır ihlali testi: yerel değişkene dışarıdan erişim denemesi
# print(gecici_parola)