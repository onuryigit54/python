# ‘kullanici_adi’ ve ‘rol’ dışarıdan gelecek verileri tutan parametrelerdir.
def kisisellestirilmis_karsilama(kullanici_adi, rol):
    print(f"Merhaba {kullanici_adi}. Sisteme ‘{rol}’ yetkisiyle bağlandınız.")

# Fonksiyon çağrılırken parantez içine gönderilen gerçek verilere "Argüman" denir.
kisisellestirilmis_karsilama("Fatih Sultan Mehmet", "Yönetici")
kisisellestirilmis_karsilama("Yahya", "Misafir")