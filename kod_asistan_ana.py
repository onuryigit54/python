# =========================================================================
# KOD-ASİSTAN PROJESİ v1.2 - MODÜLER ANA PROGRAM MOTORU (ALIAS SÜRÜMÜ)
# Standart: PEP 8 / Modül ve Fonksiyon Düzeyinde Takma İsim (as) Yönetimi
# =========================================================================
print("=== KOD-ASİSTAN: TAKMA İSİM (ALIAS) VE MODÜL TEST PANELİ ===\n")
# ------------------------------------------------------------------------
# SENARYO 1: MODÜLE TAKMA İSİM VERMEK
# asistan_finans modülü artık bu programda "fns" kısa adıyla anılacaktır.
# ------------------------------------------------------------------------
import asistan_finans as fns 
girdi_sepet_1 = 1000.0
girdi_indirim_1 = 15.0
# Çağrı yapılırken uzun modül adı yerine fns takma adı kullanılır.

sonuc_1 = fns.net_tutar_hesapla(girdi_sepet_1, girdi_indirim_1)
print(f"[SENARYO 1] fns Takma Adıyla Hesaplanan Tutar: {sonuc_1:.2f} TL")
# -----------------------------------------------------------------------
# SENARYO 2: FONKSİYONA DOĞRUDAN TAKMA İSİM VERMEK
# Modülden sadece ilgili fonksiyon çekilir ve "hesapla" ismiyle tescil edilir.
#------------------------------------------------------------------------
from asistan_finans import net_tutar_hesapla as hesapla
girdi_sepet_2 = 500.0
girdi_indirim_2 = 10.0
#Nokta (.) operatörüne gerek kalmadan doğrudan çağrılır.
sonuc_2 = hesapla(girdi_sepet_2,girdi_indirim_2)
print(f"[SENARYO 2] hesapla Fonksiyon İsimlendirmesiyle Tutar:{sonuc_2:.2f}TL")
print("==================================================")