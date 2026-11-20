# Kod-Asistan Geri Bildirim (Feedback) Arşivi
# Kullanıcı yorumlarını geri_bildirimler.txt dosyasına kalıcı olarak kaydeder
# ve yönetici için numaralandırılmış biçimde listeler.

DOSYA_ADI = "geri_bildirimler.txt"


def yorumlari_listele():
    """b, c) Arşivdeki yorumları readlines() ile okuyup numaralandırarak yazdırır."""
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            yorumlar = dosya.readlines()
    except FileNotFoundError:
        print("Sistemde kayıtlı geri bildirim bulunmamaktadır.")
        return

    if not yorumlar:
        print("Sistemde kayıtlı geri bildirim bulunmamaktadır.")
        return

    print("\n--- Geri Bildirim Arşivi ---")
    for sayac, yorum in enumerate(yorumlar, start=1):
        print(f"{sayac}. Yorum: {yorum.strip()}")


def yorum_kaydet(metin):
    """d) Yorumu 'a' modunda, eski kayıtları silmeden dosyaya ekler."""
    with open(DOSYA_ADI, "a", encoding="utf-8") as dosya:
        dosya.write(metin + "\n")


def main():
    # Yönetici ilk çalıştırmada henüz yorum yokken dosyayı okumaya çalışabilir
    print("Mevcut arşiv kontrol ediliyor...")
    yorumlari_listele()

    # ç) Kullanıcıdan geri bildirim alma
    geri_bildirim = input("\nAsistan hakkındaki geri bildiriminizi yazınız: ").strip()

    if geri_bildirim:
        yorum_kaydet(geri_bildirim)
        print("Geri bildiriminiz kaydedildi. Teşekkürler!")
    else:
        print("Boş geri bildirim kaydedilmedi.")

    # Güncel arşivi yöneticiye göster
    yorumlari_listele()


if __name__ == "__main__":
    main()