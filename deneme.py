from datetime import date

dogum_yili = int(input("Doğum yılınızı girin: "))
yas = date.today().year - dogum_yili

print(f"Yaklaşık yaşınız: {yas}")