# İki parametreli bir fonksiyon tanımı
def kullanici_tescil(isim, personel_id):
    print(f"Kullanıcı: {isim} | ID: {personel_id}")
# DOĞRU ÇAĞRI: Argümanlar parametre sırasına (str, int) tam uyumlu gönderilmiştir.
kullanici_tescil("Fatih", 1453)
# HATALI ÇAĞRI (Mantıksal Sapma): Sıra karıştırılmıştır.
kullanici_tescil(1453, "Fatih")
# Çıktı: Kullanıcı: 1453 | ID: Fatih -> Program çökmez ancak veri akışı bozulur.