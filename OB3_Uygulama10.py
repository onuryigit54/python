import turtle

# Kullanıcıdan eksen sayısını al
eksen_sayisi = int(input("Fraktal için eksen sayısını giriniz: "))

# Dönüş açısını hesapla
aci = 360 / eksen_sayisi

# Çizgi uzunluğu başlangıç değeri
cizgi_boyu = 0

# Çizim ayarları
turtle.speed(0)
turtle.pensize(2)
turtle.color("blue")

# Sonsuz döngü
while True:

    # Çizgiyi çiz ve yön değiştir
    turtle.forward(cizgi_boyu)
    turtle.left(aci)

    # Çizgi uzunluğunu 2 piksel artır
    cizgi_boyu += 2

    # Güvenlik kontrolü
    if cizgi_boyu >= 300:
        print(f"Program Güvenliği Sağlandı: 300 piksel sınırında sonsuz döngü kırıldı.")
        break

# Çizim ekranını açık tut
turtle.done()
