# pengenalan tokoh
tokoh1 = "Sarifa"
tokoh2 = "Reval"

# memulai cerita
print(f"Di sore hari, {tokoh2} pergi ke pasar tradisional di dekat rumahnya. Ia ingin membeli buah di Toko {tokoh1}")

# dialog tokoh
print(f"\n{tokoh1}:\"Hai {tokoh2}, mau beli apa hari ini?\"")
print(f"\n{tokoh2}:\"Hai, {tokoh1}. Aku mau beli apel. Berapa harganya?\"")

# input harga apel
harga_apel = int(input(f"\n{tokoh1}:\"Harga satu apel adalah RP.\""))  # menggunakan integer

# input uang reval
uang_reval = int(input("Berapa uang Reval? Rp."))  # Menggunakan integer

# Operasi aritmatika
max_beli = uang_reval // harga_apel  # Jumlah apel maksimal yang bisa dibeli reval

# Dialog
print(f"\n{tokoh2}:\"Oh, jadi satu apel harganya Rp.{harga_apel} Aku punya uang Rp.{uang_reval}\"")
if max_beli > 0:
    print(f"\n{tokoh2}:\"Berarti aku bisa beli {max_beli} apel.\"")
else:
    print(f"{tokoh2}:\"Sayangnya, uangku tidak cukup untuk membeli apel.\"")
    max_beli = 0  # Mengatur jumlah apel yang bisa dibeli menjadi 0 jika uang tidak cukup

# dialog lanjutan
reval_beli = int(input(f"\n{tokoh1}:\"Berapa apel yang mau kamu beli?\""))  # Menggunakan integer

if reval_beli <= max_beli:
    total_harga = reval_beli * harga_apel
    sisa_uang = uang_reval - total_harga
    print(f"\n{tokoh2}:\"Aku beli {reval_beli} apel.\"")
    print(f"\n{tokoh1}:\"Totalnya Rp. {total_harga}. Uangmu tersisa Rp.{sisa_uang}\"")
else:
    print(f"\n{tokoh1}:\"Maaf, kamu tidak bisa membeli sebanyak itu. Uangmu tidak cukup.\"")
    sisa_uang = uang_reval # pastikan sisa uang terdefinisi

if sisa_uang > 0:
    beli_lagi = input(f"\n{tokoh1}:\"Ada lagi yang ingin kamu beli?\" (ya/tidak): ").strip().lower()
    if beli_lagi == 'ya':
        # Menanyakan harga item tambahan
        print(f"\n{tokoh2}:\"Kalau buah jeruk ini harganya berapa?\"")
        harga_jeruk = int(input(f"\n{tokoh1}:\"Harganya RP.\""))
        # Menghitung jumlah item tambahan yang bisa dibeli
        max_beli_lagi = sisa_uang // harga_jeruk
        if max_beli_lagi > 0:
            beli_jeruk = int(input(f"\n{tokoh1}:\"Berapa buah yang ingin kamu beli? (maksimal {max_beli_lagi}):\""))
            if beli_jeruk <= max_beli_lagi:
                total_beli_lagi = beli_jeruk * harga_jeruk
                sisa_uang -= total_beli_lagi
                print(f"\n{tokoh2}:\"Aku beli {beli_jeruk} buah.\"")
                print(f"\n{tokoh1}:\"Totalnya Rp.{total_beli_lagi}. Uangmu tersisa Rp.{sisa_uang}\"")
            else:
                print(f"\n{tokoh1}:\"Maaf, kamu tidak bisa membeli sebanyak itu. Uangmu tidak cukup.\"")
        else:
            print(f"\n{tokoh1}:\"Maaf, uangmu tidak cukup untuk membeli item tambahan.\"")
    else:
        print(f"\n{tokoh2}:\"Tidak ada yang ingin aku beli lagi.\"")
else:
    print(f"\n{tokoh2}:\"Tidak ada lagi yang bisa aku beli. Uangku sudah habis.\"")

# Dialog penutup
print(f"\n{tokoh2}:\"Terima kasih, {tokoh1}.\"")
print(f"\n{tokoh1}:\"Sama-sama, {tokoh2}. Sampai jumpa lagi.\"")
print(f"\nAkhirnya {tokoh2} pulang dan membawa buah yang dibelinya.")
