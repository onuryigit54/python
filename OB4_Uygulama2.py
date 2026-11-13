# Dijital Oyun Motoru: Karakter Hasar Mekanizması
# Algoritma tasarımında yardımcı olan takım arkadaşı: [TAKIM ARKADAŞININ ADI SOYADI]


def hasar_al(mevcut_can, darbe_gucu, kalkan=0):
    """Karakterin aldığı net hasarı hesaplar ve kalan canı ekrana yazdırır.

    mevcut_can: Karakterin darbeden önceki canı
    darbe_gucu: Gelen darbenin gücü
    kalkan: Kalkan puanı (varsayılan 0, yani kalkan yok)
    """
    # Kalkan puanı darbe gücünden düşülür, net hasar negatif olamaz.
    net_hasar = max(0, darbe_gucu - kalkan)
    kalan_can = mevcut_can - net_hasar

    if kalkan > 0:
        durum = "Kalkan darbeyi emdi."
    else:
        durum = "Kalkan yok."

    # Yapay zeka denetiminden sonra eklenen kontrol: can 0'ın altına düşerse oyun biter.
    if kalan_can < 0:
        print("Oyun Bitti")
    else:
        print(f"Kahraman darbe aldı! {durum} Kalan Can: {kalan_can}")

    return kalan_can


# 1. Senaryo: Kalkansız yalın hasar
hasar_al(100, 30)

# 2. Senaryo: Kalkan aktif, değeri ezme
hasar_al(100, 30, 10)

# Ek test: can 0'ın altına düşer
hasar_al(20, 50)