print("--- KOD-ASİSTAN SİSTEM DENETİMİ ---")
# input() yerleşik fonksiyonu, akışı durdurur ve dinamik veri alır.
sistem_kodu = input("Lütfen sistem onay kodunu giriniz: ")
# len() yerleşik fonksiyonu, verinin boyutunu (karakter sayısını) ölçer.
kod_uzunlugu = len(sistem_kodu)
# type() bellek türünü analiz ederken, print() sonucu ekrana yansıtır.
print(f"Girdiğiniz kod {kod_uzunlugu} karakterden oluşmaktadır.")
print("Bellekteki veri türü:", type(sistem_kodu))