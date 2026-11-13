# break ve continue Mantığının Gösterimi
for sayi in range(1, 10):
    if sayi == 3:
        continue # 3 sayısı görüldüğünde ekrana yazdırma turu atlanır.
    if sayi == 5:
        break    # 5 sayısı görüldüğünde döngü tamamen sonlandırılır.
    print(f"İşlenen Sayı: {sayi}")