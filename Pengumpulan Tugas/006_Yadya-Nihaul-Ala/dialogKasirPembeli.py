
from tabulate import tabulate
# <<<<<< Daftar harga barang >>>>>>
harga_barang = {
    "Sosro": 6000,
    "Aqua": 4000,
    "Milo": 10000,
    "Sprite": 9000,
    "Pocari": 11000,
    "Cimory": 12000,
    "Fanta": 5000,
    "Mizone": 8000,
    "Golda": 3000,
    "Indomilk": 7000,
    "Milku": 4000,
    "Yakult": 3000
}

tabel_data = [(barang, harga) for barang, harga in harga_barang.items()]

print("Kasir: Selamat datang! Berikut adalah daftar minuman yang tersedia:")
print(tabulate(tabel_data, headers=["Barang", "Harga per Unit"], tablefmt="grid"))

nama_barang = input("Pembeli: Aku ingin membeli ")

if nama_barang in harga_barang:
    jumlah_barang = int(input(f"Kasir: Berapa banyak {nama_barang} yang ingin Anda beli? "))

    # Diskon untuk beberapa minuman
    if nama_barang in ["Milku", "Yakult", "Sosro", "Milo", "Aqua"]:
        if jumlah_barang == 1:
            tambah_diskon = input(f"Kasir: Tambah 1 {nama_barang} lagi untuk mendapatkan diskon beli 2 potongan 2000, apakah Anda tertarik? (yes/no): ").lower()
            if tambah_diskon == "yes":
                jumlah_barang += 1
                print(f"Kasir: Anda mendapatkan diskon sebesar 2000 karena membeli 2 {nama_barang}!")
                total_harga = jumlah_barang * harga_barang[nama_barang] - 2000
            else:
                total_harga = jumlah_barang * harga_barang[nama_barang]
        else:
            if jumlah_barang >= 2:
                total_harga = jumlah_barang * harga_barang[nama_barang] - 2000
                print(f"Kasir: Anda mendapatkan diskon sebesar 2000 karena membeli {jumlah_barang} {nama_barang}!")
            else:
                total_harga = jumlah_barang * harga_barang[nama_barang]
    else:
        # tanpa diskon
        total_harga = jumlah_barang * harga_barang[nama_barang]
    
    print(f"Kasir: Anda memilih {jumlah_barang} {nama_barang}.")
    print(f"Kasir: Harga per unit adalah {harga_barang[nama_barang]}.")
    print(f"Kasir: Total harga yang harus dibayar adalah {total_harga}.")

    uang_dibayar = int(input("Pembeli: Aku membayar "))

    while uang_dibayar < total_harga:
        print(f"Kasir: Uang Anda kurang {total_harga - uang_dibayar}.")
        tambahan_uang = int(input("Pembeli: Oh, maaf! Ini uang saya "))
        uang_dibayar += tambahan_uang
    
    kembalian = uang_dibayar - total_harga
    print(f"Kasir: Uang yang Anda bayarkan: {uang_dibayar}.")
    print(f"Kasir: Kembalian Anda: {kembalian}.")
    
    print("Kasir: Terima kasih sudah berbelanja di sini!")
else:
    print("Kasir: Maaf, minuman yang Anda masukkan tidak tersedia.")
